## Copyright (c) 2018, Blake C. Rawlings.
##
## This file is part of `st2smv`.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import json
import os
import pprint
import re
import shutil
import subprocess
import tempfile
import time

from . import smv
from . import utils

logger = utils.logging.getLogger(__name__)

CAN_MEET_RELAXED = 'The task CAN meet the relaxed deadline'
CAN_NOT_MEET_RELAXED = 'The task can NOT meet the relaxed deadline'
BMC_BASE_TIMEOUT = 30.0
BMC_TIMEOUT_FACTOR = 4
BMC_FALL_BACK_ON_FULL_MC = False # TODO: command-line option


def check_schedule(args=None):
    """Read a schedule and the current state of the plant from file and
    check whether the schedule is feasible (i.e., can be completed
    from the current state).

    """
    assert args is not None # TODO: error message
    ## Read the data.
    with open(args.input[0]) as f:
        schedule = json.load(f)
    logger.info('Checking the schedule:\n{}'.format(pprint.pformat(schedule)))
    with open(args.input[1]) as f:
        state = json.load(f)
        logger.info('In the current state:\n{}'.format(pprint.pformat(state)))
    state_path = read_current_state(
        args.input[1], directory=args.output_directory
    )
    ## Sort the tasks.
    tasks = []
    for unit in schedule['tasks']:
        for task in schedule['tasks'][unit]:
            tasks.append(tuple([unit] + task))
    tasks.sort(key=(lambda x: x[2][1]))
    assert len(tasks) > 0 # TODO: error message
    active_tasks = [
        task
        for task in tasks
        if (task[2][0] <= state['time'] and state['time'] <= task[2][1])
    ]
    if args.key_scheduling_unit is not None:
        key_tasks = [
            task
            for task in active_tasks
            if task[0] == args.key_scheduling_unit
        ]
    else:
        key_tasks = active_tasks
    if len(key_tasks) > 1:
        logger.warning('More than one task is active: {}'.format(key_tasks))
    elif len(key_tasks) == 0:
        logger.warning('No active tasks; not checking the schedule.')
    ## Go through the tasks (in order) and check whether the deadlines
    ## can be met.
    detected_infeasibility = False
    counts = {} # track which tasks were (or could have been) completed already
    _write_output(args.output_directory, ['--'], 'path.cex')
    for task in key_tasks[:1]: # only check the first task
        is_feasible = None
        ## Create a "subschedule" with only one task (this one).
        subschedule = schedule.copy()
        subschedule['tasks'] = {task[0]: [[task[1], task[2]]]}
        (feasible_horizon, cex, bmc_solve_times, bmc_timeout) = _run_bmc(
            subschedule, state_path, args=args
        )
        if feasible_horizon is not None:
            if feasible_horizon <= task[2][1]:
                ## The approximate bound already meets the deadline.
                is_feasible = True
                assert args.output_directory is not None
                logger.info('Task CAN meet the deadline: {}'.format(task))
                _write_output(args.output_directory, cex, 'path.cex')
            else:
                ## The best feasible end time found via BMC doesn't meet the
                ## deadline, so either trust BMC (which is not theoretically
                ## valid) or use full model checking to get a sound result.
                mean_bmc_solve_time = (
                    sum(bmc_solve_times) / len(bmc_solve_times)
                )
                max_bmc_solve_time = max(bmc_solve_times)
                logger.warning('BMC was inconclusive.')
                logger.debug(
                    'BMC solve times (in seconds): {}.'
                    .format(bmc_solve_times)
                )
                logger.info(
                    'Mean BMC solve time: {:.2g} seconds.'
                    .format(mean_bmc_solve_time)
                )
                logger.info(
                    'Max BMC solve time: {:.2g} seconds.'
                    .format(max_bmc_solve_time)
                )
                logger.info(
                    'Final BMC timeout: {:.2g} seconds.'
                    .format(bmc_timeout)
                )
                if bmc_timeout >= BMC_TIMEOUT_FACTOR * max_bmc_solve_time:
                    ## There /probably/ isn't any better feasible deadline.
                    is_feasible = False # N.B.: heuristic!
                    logger.info(
                        'Task (PROBABLY) can NOT meet the deadline: {}; '
                        'skipping full model checking.'
                        .format(task)
                    )
                    _write_output(args.output_directory, cex, 'path.cex')
                    _record_known_delay(
                        state, schedule, task, feasible_horizon - 1, args
                    )
                    detected_infeasibility = True
                else:
                    ## Shorten the horizon to speed up the subsequent checks.
                    logger.warning('The BMC timeout was too aggressive.')
                    subschedule['horizon'][1] = feasible_horizon
        if is_feasible is None:
            if BMC_FALL_BACK_ON_FULL_MC:
                logger.info('Resorting to full model checking...')
                detected_infeasibility = _run_mc(
                    subschedule, state_path, state, schedule, task, args=args
                )
            else:
                logger.warning('Skipping the full model checking run...')
        ## Stop early if part of the schedule is infeasible.
        if detected_infeasibility:
            break
        else:
            ## Record this task as having been completed.
            utils.try_incr(counts, (task[0], task[1]), 1)
            continue
    ## Repeat the schedule+state after all the solver output.
    logger.info('The schedule was:\n{}'.format(pprint.pformat(schedule)))
    logger.info('The state was:\n{}'.format(pprint.pformat(state)))


def _run_bmc(subschedule, state_path, args=None):
    """Use bounded model checking to approximate the minimum feasible deadline.

    BMC (without a rigorous bound) doesn't guarantee that a particular deadline
    is infeasible, but it can produce a sequence of feasible deadlines that can
    then serve as a starting point for complete BDD-based model checking.

    """
    ## Write the model.
    model_path = _combine_model_files(
        subschedule, state_path, args=args
    )
    ## Get the baseline specification, with no deadline.
    deadlines = _get_task_deadlines(subschedule)
    assert len(deadlines) == 1 # TODO: handle multiple active tasks
    label = sorted(deadlines)[0]
    assert len(label) == 2
    counter_var = 'COUNT_{}_{}'.format(*label)
    assert len(deadlines[label]) == 1 # TODO: handle multiple active tasks
    (count, deadline) = deadlines[label][0]
    bmc_spec = 'LTLSPEC G({} < {});'.format(counter_var, count)
    ## Approximate the minimum feasible deadline.
    final_time = None
    counterexample = None
    solve_times = []
    bmc_timeout = BMC_BASE_TIMEOUT
    while True:
        bmc_model_path = os.path.dirname(model_path) + os.path.sep + 'bmc.smv'
        shutil.copy(model_path, bmc_model_path)
        with open(bmc_model_path, 'a') as f:
            f.writelines([bmc_spec])
            f.flush()
        ## Run the solver, with a timeout.
        with tempfile.TemporaryFile() as f:
            ## `subprocess.PIPE`, etc., don't seem to work well on Windows, so
            ## use a temporary file for the output instead.
            proc = subprocess.Popen(
                [
                    args.solver_path,
                    '-bmc', '-bmc_length', '100',
                    bmc_model_path,
                ],
                stdout=f, stderr=subprocess.STDOUT,
            )
            elapsed = _kill_process_after_timeout(proc, timeout=bmc_timeout)
            f.seek(0)
            out = str(f.read())
        ## Find the final time in the counterexample.
        if 'is false' in out:
            assert elapsed is not None
            solve_times.append(elapsed)
            times = map(int, re.findall(r'\s*time\s+=\s+([0-9]+)\s*', out))
            final_time = max(times)
            counterexample = out.split(os.linesep)
            logger.debug('A feasible deadline: {}'.format(final_time))
            bmc_spec = 'LTLSPEC G(!(({} >= {}) & (time < {})));'.format(
                counter_var, count, final_time
            )
            if final_time <= deadline:
                break
            else:
                ## Set the timeout based on the actual required solve time.
                bmc_timeout = BMC_TIMEOUT_FACTOR * max(solve_times)
                continue
        else:
            logger.debug(
                'Did not find {} feasible deadline, giving up.'
                .format('any' if final_time is None else 'a better')
            )
            break
    if final_time is None:
        logger.warning('Did not find any feasible deadline via BMC.')
    else:
        logger.info('Found a feasible deadline via BMC: {}'.format(final_time))
    return (final_time, counterexample, solve_times, bmc_timeout)


def _run_mc(
        subschedule, state_path, state, schedule, task,
        args=None, counts=None,
):
    """Use full model checking to calculate the minimum feasible deadline.

    Unlike BMC, full model checking /can/ guarantee that a particular deadline
    is infeasible (assuming that the model is an abstraction of the actual
    process).

    """
    detected_infeasibility = False
    assert args.output_directory is not None # TODO: error message
    model_path = _combine_model_files(
        subschedule, state_path, args=args, initial_counts=counts
    )
    solver = smv.SolverCommunicator(
        args.solver_path, args.solver_arguments.split(), model_path
    )
    (is_feasible, cex) = _check_deadline(
        subschedule, solver, args=args, initial_counts=counts
    )
    if is_feasible is True:
        logger.info('Task CAN meet the deadline: {}'.format(task))
        _write_output(args.output_directory, cex, 'path.cex')
    elif is_feasible is False:
        logger.info('Task can NOT meet the deadline: {}'.format(task))
        detected_infeasibility = True
        deadline = task[2][1]
        horizon = subschedule['horizon'][1]
        assert horizon >= deadline # TODO: error message
        ## Exponential search.
        k = 0
        lower = deadline
        upper = None
        while True:
            if args.debug_args is not None:
                if 'simple_delay' in args.debug_args:
                    ## Just report a delay of 1 (which is valid).
                    upper = lower + 1
                    break
            else:
                logger.debug(
                    'Attempting to determine how long the delay will be...'
                )
            relaxation = 2**k
            relaxed_deadline = min([deadline + relaxation, horizon])
            logger.debug(
                'Checking relaxed deadline: {}'.format(relaxed_deadline)
            )
            subschedule = {
                'tasks': {
                    task[0]: [[task[1], [task[2][0], relaxed_deadline]]]
                }
            }
            (is_feasible, cex) = _check_deadline(
                subschedule, solver, args=args, initial_counts=counts
            )
            if is_feasible is True:
                logger.debug(CAN_MEET_RELAXED)
                upper = relaxed_deadline # TODO: get a tighter bound from
                                         # the counterexample trace
                _write_output(args.output_directory, cex, 'path.cex')
                break
            elif is_feasible is False:
                logger.debug(CAN_NOT_MEET_RELAXED)
                lower = relaxed_deadline
                _record_known_delay(state, schedule, task, lower, args)
            else:
                assert False # TODO: error message
            ##
            if relaxed_deadline == horizon:
                break
            else:
                k += 1
        ## Binary search.
        if upper is None:
            logger.info('Could not find an upper bound for the delay.')
        else:
            while (upper - lower) >= 2:
                middle = int((upper + lower) / 2)
                logger.debug(
                    'Checking the relaxed deadline: {}'.format(middle)
                )
                subschedule = {
                    'tasks': {
                        task[0]: [[task[1], [task[2][0], middle]]]
                    }
                }
                (is_feasible, cex) = _check_deadline(
                    subschedule, solver,
                    args=args, initial_counts=counts,
                )
                if is_feasible is True:
                    logger.debug(CAN_MEET_RELAXED)
                    upper = middle
                    _write_output(args.output_directory, cex, 'path.cex')
                elif is_feasible is False:
                    logger.debug(CAN_NOT_MEET_RELAXED)
                    lower = middle
                    _record_known_delay(state, schedule, task, lower, args)
                else:
                    assert False # TODO: error message
            logger.info(
                'The maximum INFEASIBLE deadline: {}'.format(lower)
            )
            _record_known_delay(state, schedule, task, lower, args)
    else:
        assert False # TODO: error message
    return detected_infeasibility


def _kill_process_after_timeout(process, timeout=10.0, increment=0.1):
    assert timeout > 0 and increment > 0
    elapsed = 0
    while True:
        if process.poll() is not None:
            break
        elif elapsed >= timeout:
            process.kill()
            process.wait() # needed after `.kill()` on Windows?
            elapsed = None
            break
        else:
            time.sleep(increment)
            elapsed += increment
            continue
    return elapsed


def _record_known_delay(state, schedule, task, lower, st2smv_args):
    delay_info = {
        'time': state['time'],
        'absolute_time': state['_absolute_time'],
        'horizon': schedule['horizon'],
        'task': task,
        'delay': lower - task[2][1] + 1,
    }
    _write_output(
        st2smv_args.output_directory,
        delay_info,
        'delay.json',
        as_json=True,
    )


def read_current_state(path, directory):
    """Read the current state from the plant."""
    lines = ['-- Current state.']
    with open(path) as f:
        data = json.load(f)
    for var in data:
        if var.startswith('_'):
            continue
        val = data[var]
        if isinstance(val, bool):
            lines.append('INIT {}{};'.format('!' if not val else '', var))
        elif isinstance(val, int):
            lines.append('INIT {} = {};'.format(var, val))
        else:
            assert False # TODO: error message
    return _write_output(directory, lines, 'state.smv')


def _combine_model_files(
        subschedule, state_path, args=None, initial_counts=None
):
    assert isinstance(subschedule, dict)
    assert isinstance(state_path, utils.six.string_types)
    assert args is not None
    ## Create a specification from the subschedule.
    lines = read_schedule(subschedule, initial_counts=initial_counts)
    subschedule_path = _write_output(
        args.output_directory, lines, 'subschedule.smv'
    )
    ## Locate the necessary metadata files for the subschedule.
    assert len(args.metadata) <= 1 # TODO: error message
    extra_files = []
    for path in args.metadata:
        with open(path) as f:
            metadata = json.load(f)
        if '*' in metadata:
            extra_files += metadata['*']
        for unit in subschedule['tasks']:
            for operation in subschedule['tasks'][unit]:
                try:
                    extra_files += metadata[unit][operation[0]]
                except KeyError:
                    logger.warning(
                        'No metadata found for task {}'
                        .format((unit, operation[0]))
                    )
    ## Run SynthSMV.
    cmd = [
        'st2smv', '--verbosity', 'error',
        '--combine',
        '--input', subschedule_path, state_path,
    ] + args.input[2:] + extra_files # TODO: plugins+options
    if len(args.plugins) > 0:
        cmd += ['--plugins'] + args.plugins
    if len(args.plugin_options) > 0:
        cmd += ['--plugin-options'] + args.plugin_options
    if args.variables is not None:
        cmd += ['--variables'] + args.variables
    logger.debug(
        'Combining the necessary files to check the subschedule:\n{}'
        .format(' '.join(cmd))
    )
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    combined = proc.communicate()[0].decode().split('\n')
    combined_path = _write_output(
        args.output_directory, combined, 'combined.smv'
    )
    return combined_path


def _check_deadline(schedule, solver, args=None, initial_counts=None):
    assert isinstance(schedule, dict)
    assert args is not None
    target = _get_first_target(schedule, initial_counts=initial_counts)
    path = solver.get_path(target)
    if path is None:
        return (False, None)
    else:
        cex = path.split(os.linesep)
        return (True, cex)


def _get_first_target(schedule, initial_counts=None):
    ## Sort the tasks by end time.
    unordered = []
    for unit in schedule['tasks']:
        for item in schedule['tasks'][unit]:
            unordered.append([unit] + item)
    ordered = sorted(unordered, key=(lambda x: x[2][1]))
    ## Set up the task counters.
    if initial_counts is None:
        counts = {}
    else:
        assert isinstance(initial_counts, dict)
        counts = initial_counts.copy()
    ## Take the first task (TODO: check that it's currently in progress)
    task = ordered[0]
    utils.try_incr(counts, (task[0], task[1]), 1)
    target = '({} = {}) & (time <= {})'.format(
        'COUNT_{}_{}'.format(task[0], task[1]),
        counts[(task[0], task[1])],
        task[2][1],
    )
    return target


def read_schedule(schedule, directory=None, initial_counts=None):
    """Read a schedule from file and convert it to a specification to
    check its feasibility.

    """
    if isinstance(schedule, utils.six.string_types):
        with open(schedule) as f:
            data = json.load(f)
    else:
        assert isinstance(schedule, dict)
        data = schedule
    assert {'horizon', 'tasks'} <= set(data)
    for unit in data['tasks']:
        for task in data['tasks'][unit]:
            ## Every task has to finish before the horizon.
            assert task[1][1] <= data['horizon'][1]
    ## Determine the horizon (and beginning) of the schedule.
    lines = ['-- Schedule.']
    lines += [
        'DEFINE HORIZON_begin := {};'.format(data['horizon'][0]),
        'DEFINE HORIZON_end := {};'.format(data['horizon'][1]),
    ]
    ## Detect the "deadlines" for the tasks and create specifications
    ## from the schedule.
    (counters, specs) = _get_deadline_specifications(
        data, initial_counts=initial_counts
    )
    lines += counters + specs
    ##
    if directory is not None:
        _write_output(directory, lines, 'schedule.smv')
        return None
    else:
        return lines


def _get_deadline_specifications(data, initial_counts=None):
    ## Sort the tasks by end time.
    unordered = []
    for unit in data['tasks']:
        for item in data['tasks'][unit]:
            unordered.append([unit] + item)
    ordered = sorted(unordered, key=(lambda x: x[2][1]))
    ## Create a specification that each task be able to finish "on
    ## time".
    specification_lines = []
    if initial_counts is None:
        counts = {}
    else:
        assert isinstance(initial_counts, dict)
        counts = initial_counts.copy()
    for task in ordered:
        utils.try_incr(counts, (task[0], task[1]), 1)
        specification_lines.append(
            '-- SPEC AG(!(({} = {}) & (time <= {})));'.format(
                'COUNT_{}_{}'.format(task[0], task[1]),
                counts[(task[0], task[1])],
                task[2][1],
            )
        )
    ## Create the counter variables.
    counter_lines = []
    for counter in counts:
        if initial_counts is not None:
            if counter in initial_counts:
                if counts[counter] <= initial_counts[counter]:
                    ## The (sub)schedule under consideration doesn't include
                    ## this task type, so it won't appear in the specification,
                    ## so the counter isn't necessary (even though one or more
                    ## of this task type was completed previously).
                    continue
        var_name = 'COUNT_{}_{}'.format(counter[0], counter[1])
        counter_lines += [
            'VAR {} : 0..{};'.format(var_name, counts[counter]),
            'INIT {} = 0;'.format(var_name),
        ]
    ##
    return (counter_lines, specification_lines)


def _get_task_deadlines(data, initial_counts=None):
    ## Sort the tasks by end time.
    unordered = []
    for unit in data['tasks']:
        for item in data['tasks'][unit]:
            unordered.append([unit] + item)
    ordered = sorted(unordered, key=(lambda x: x[2][1]))
    ## Extract the "count" and "end time" for each task.
    deadlines = {}
    if initial_counts is None:
        counts = {}
    else:
        assert isinstance(initial_counts, dict)
        counts = initial_counts.copy()
    for task in ordered:
        label = (task[0], task[1])
        end_time = task[2][1]
        if label not in deadlines:
            deadlines[label] = []
        utils.try_incr(counts, label, 1)
        count = counts[label]
        deadlines[label].append((count, end_time))
    return deadlines


def _write_output(directory, data, file_name, as_json=False):
    if as_json is False:
        assert isinstance(data, (list, tuple))
    else:
        assert isinstance(data, dict)
    if directory is None:
        if as_json is False:
            print(os.linesep.join(data))
        else:
            pprint.pprint(data)
        return None
    else:
        if not os.path.isdir(directory):
            os.mkdir(directory)
        path = directory + os.sep + file_name
        with open(path, 'w') as f:
            if as_json is False:
                f.writelines([line.rstrip() + os.linesep for line in data])
            else:
                json.dump(data, f)
        return path


def read_timing_data(path, directory=None):
    """Read historical step timing information and a description of how it
    maps to the process.

    """
    with open(path) as f:
        timing_data = json.load(f)
    lines = [
        '-- "Global" process time.',
        'VAR time : HORIZON_begin..HORIZON_end;',
        'TRANS next(time) >= time;',
    ]
    for label in timing_data:
        lines += [''] + _get_timing_logic(timing_data, label)
    lines += [''] + _get_initial_state_constraints(timing_data)
    _write_output(directory, lines, 'timing.smv')


def _get_timing_logic(timing_data, unit_label):
    unit = timing_data[unit_label]
    lines = ['-- Step timing information for unit `{}`.'.format(unit_label)]
    ## Variable declarations.
    lines.append('VAR {}_t0 : HORIZON_begin..HORIZON_end;'.format(unit_label))
    ## Reset the start time after a step transition.
    lines.append(
        'TRANS next({0}_t0) = ((count({1}) > 0) ? next(time) : {0}_t0);'
        .format(
            unit_label,
            ', '.join(['{0} != next({0})'.format(step) for step in unit]),
        )
    )
    ## Increment the time after a step is completed.
    for step in unit:
        if isinstance(unit[step], int):
            ## The step time does not depend on any process variables.
            if unit[step] == 0:
                pass # no need to do anything for "timeless" steps
            else:
                assert unit[step] > 0
                lines.append(
                    'TRANS {1} & !next({1})'
                    ' -> '
                    'next(time) >= {0}_t0 + {2};'
                    .format(unit_label, step, unit[step])
                )
        elif isinstance(unit[step], dict):
            ## The step time /does/ depend on "indicator" variables.
            for indicator in unit[step]:
                lines.append(
                    'TRANS {1} & !next({1})'
                    ' -> '
                    'next(time) >= {0}_t0 + ({2} ? {3} : 0);'
                    .format(unit_label, step, indicator, unit[step][indicator])
                )
    return lines


def _get_initial_state_constraints(timing_data):
    lines = ['-- One and only one step is active at a time.']
    for unit in timing_data:
        lines.append('INIT count({}) = 1;'.format(
            ', '.join(timing_data[unit])
        ))
    return lines
