#!/usr/bin/env python
import argparse
import ConfigParser

from usbtmc.scope import Scope
from usbtmc.siggen import Siggen, Function


WAVESPERSCREEN = 5


def get_args():
    parser = argparse.ArgumentParser(description="Pseudo VNA using a Siggen and Scope")
    parser.add_argument("siggen", help="Siggen device file")
    parser.add_argument("scope", help="Scope device file")
    parser.add_argument("config", help="Config file")
    parser.add_argument("output", help="Output file")
    return parser.parse_args()


def f_to_td(f):
    return round((1/float(f))/WAVESPERSCREEN, 10)


def main(siggen, scope, config, output_file):
    sweep_start = int(float(config.get('Sweep', 'start')))
    sweep_end = int(float(config.get('Sweep', 'end')))
    sweep_step = int(float(config.get('Sweep', 'step')))
    sweep_range = range(sweep_start, sweep_end, sweep_step)

    siggen_channel = int(config.get('Channels', 'source'))
    scope_ref = int(config.get('Channels', 'reference'))
    scope_ret = int(config.get('Channels', 'return'))
    scope_other = int(config.get('Channels', 'other'))

    # Init
    siggen.set_load_impedance(siggen_channel, 50)
    siggen.func(siggen_channel, Function.SINE)
    siggen.output_on(siggen_channel)

    old_td = f_to_td(sweep_start)
    scope.set_time(old_td)

    for sweep_freq in sweep_range:
        print "Freq: {0}".format(sweep_freq)
        # new_td = f_to_td(sweep_freq)
        # if old_td - new_td >= 0.5e-9:
        #     old_td = new_td
        #     scope.set_time(new_td)
        #     print "Set scope to {0}ns/div".format(new_td/1e-9)
        siggen.frequency(siggen_channel, sweep_freq)

        scope.capture([scope_ref, scope_ret, scope_other])

        meas_f = scope.get_freq(scope_ref)
        meas_phase = scope.get_phase(scope_ref, scope_ret)
        meas_ref_v = scope.get_rmsac(scope_ref)
        meas_ret_v = scope.get_rmsac(scope_ret)
        meas_other_v = scope.get_vavg(scope_other)

        output_file.write("{0},{1},{2},{3},{4},{5}\n".format(sweep_freq, meas_f, meas_phase, meas_ref_v, meas_ret_v, meas_other_v))

    siggen.output_off(siggen_channel)
    output_file.close()


if __name__ == "__main__":
    args = get_args()

    siggen = Siggen(args.siggen)
    scope = Scope(args.scope)

    config = ConfigParser.ConfigParser()
    config.read(args.config)

    output_file = open(args.output, 'w')

    try:
        main(siggen, scope, config, output_file)
    except KeyboardInterrupt:
        siggen.output_off(1)
