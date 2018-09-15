# -*- coding: utf8 -*-
import json
import click
import click.types
from six import wraps

from missinglink_commands.legit.api import ApiCaller
from missinglink_commands.legit.context import init_context2
from missinglink_commands.utilities.default_params import get_default


def _complete_type(ctx, resources, element_name, show_org=True):
    if ctx.obj is None:
        init_context2(ctx)

    resources_result = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', resources)

    resources_result = resources_result.get(resources, [])

    orgs = set([project.get('org', 'me') for project in resources_result]) if show_org else []

    result = []
    for resource in resources_result:
        project_id = str(resource[element_name])

        display_name = resource.get('display_name')

        if len(orgs) > 1:
            org = resource.get('org', 'me')

            display_name += ' @' + org

        result.append((project_id, display_name))

    return result


class DataVolumeIdParamType(click.types.IntParamType):
    # noinspection PyMethodMayBeStatic
    def complete(self, ctx, _incomplete):
        return _complete_type(ctx, 'data_volumes', 'id')


class ProjectIdParamType(click.types.IntParamType):
    # noinspection PyMethodMayBeStatic
    def complete(self, ctx, _incomplete):
        return _complete_type(ctx, 'projects', 'project_id')


class OrganizationParamType(click.types.StringParamType):
    # noinspection PyMethodMayBeStatic
    def complete(self, ctx, _incomplete):
        return _complete_type(ctx, 'orgs', 'org', show_org=False)


class DataVolumeOptions(object):
    @staticmethod
    def isolation_token_option():
        def decorator(f):
            return click.option('--isolation-token', required=False)(f)

        return decorator

    @staticmethod
    def data_volume_id_argument(required=True):
        def prompt_volume_id(ctx, param, value):
            return CommonOptions._complete_type_callback(ctx, param, value, required, 'volume_id', 'Select Data Volume')

        def decorator(f):
            return click.argument(
                'volume-id', type=DataVolumeIdParamType(), callback=prompt_volume_id, required=False, envvar='VOLUMEID')(f)

        return decorator

    @staticmethod
    def data_path_option(required=True):
        def decorator(f):
            return click.option('--data-path', required=required, help='Path to the data')(f)

        return decorator


class CommonOptions(object):
    @staticmethod
    def processes_option():
        def decorator(f):
            return click.option('--processes', default=-1, type=int, required=False)(f)

        return decorator

    @staticmethod
    def no_progressbar_option():
        def decorator(f):
            return click.option('--no-progressbar/--enable-progressbar', default=False, is_flag=True, required=False)(f)

        return decorator

    @staticmethod
    def _check_required(ctx, param, required):
        def true_decorator(f):
            @wraps(f)
            def wrap(*args, **kwargs):
                value = f(*args, **kwargs)

                if value is None and required:
                    raise click.MissingParameter(ctx=ctx, param=param)

                return value

            return wrap

        return true_decorator

    @staticmethod
    def alert_type_option(required=False, multiple=False):
        all_options = ['started', 'stopped', 'ended', 'failed', 'data-warning']

        def validate_alert_type(ctx, option, value):
            def normalize_value(current_value):
                for alert_type in current_value:
                    if alert_type == 'all':
                        current_value.extend(all_options)

                return_value = [v for v in current_value if v in all_options]

                return list(set(return_value))

            def ask_for_value():
                import inquirer
                questions = [
                    inquirer.Checkbox(
                        'alert',
                        message="Select Alerts",
                        choices=all_options,
                    ),
                ]
                answers = inquirer.prompt(questions)

                return answers['alert']

            @CommonOptions._check_required(ctx, option, required)
            def wrap():
                actual_value = value if value else ask_for_value()

                return normalize_value(list(actual_value))

            return wrap()

        def decorator(f):
            return click.option(
                '--alert-type', '-a', callback=validate_alert_type, type=click.Choice(['all'] + all_options), required=False, multiple=multiple,
                help='Alert type for project subscription')(f)

        return decorator

    @staticmethod
    def org_option(required=True):
        def prompt_org_id(ctx, param, value):
            return CommonOptions._complete_type_callback(ctx, param, value, required, 'org', 'Select Organization')

        def decorator(f):
            return click.option('--org', required=False, callback=prompt_org_id, envvar='ML_ORG',
                                type=OrganizationParamType(), help='organization to use')(f)

        return decorator

    # noinspection PyShadowingBuiltins
    @staticmethod
    def project_id_option(required=False, multiple=False, help=None):
        def prompt_project_id(ctx, param, value):
            return CommonOptions._complete_type_callback(ctx, param, value, required, 'project', 'Select Project')

        def decorator(f):
            return click.option(
                '--project', '-p', type=ProjectIdParamType(), envvar='ML_PROJECT',
                callback=prompt_project_id, required=False, multiple=multiple,
                help=help or 'The project Id. Use `ml projects list` to find your project Ids')(f)

        return decorator

    @staticmethod
    def experiment_id_option(required=False):
        def decorator(f):
            return click.option(
                '--experiment', '-e', type=int, metavar='<int>', required=required,
                help='The experiment ID. Use `ml experiments list` to find your experiment IDs')(f)

        return decorator

    @staticmethod
    def _complete_type_callback(ctx, param, value, required, name, prompt):
        def nice_display_name(item):
            resource_id, display_name = item

            if display_name:
                return '%s - %s' % (resource_id, display_name)

            return str(resource_id)

        def ask_for_value(options):
            import inquirer
            choices = list(map(nice_display_name, options))

            questions = [
                inquirer.List(
                    name,
                    message=prompt,
                    choices=choices,
                ),
            ]
            answers = inquirer.prompt(questions)

            resource_parts = answers[name].split(' - ')

            return resource_parts[0]

        @CommonOptions._check_required(ctx, param, required)
        def wrap():
            if value or not required:
                return value

            value_from_default = get_default(name)

            if value_from_default is not None:
                return value_from_default

            lst = param.type.complete(ctx, None)

            if len(lst) == 1:
                return lst[0][0]

            return ask_for_value(lst)

        return wrap()

    @staticmethod
    def validate_json(ctx, param, value):
        try:
            if value is None:
                return None

            return json.loads(value)
        except ValueError:
            raise click.BadParameter('not valid json', param=param, ctx=ctx)


class ChartsOptions(object):
    @staticmethod
    def chart_scope_option(required=False):
        def decorator(f):
            return click.option(
                '--chart-scope', '-cs', type=click.Choice(['test', 'validation', 'train']), required=required,
                default='test', help='Scope type.')(f)

        return decorator

    @staticmethod
    def chart_type_option(required=False):
        def decorator(f):
            return click.option(
                '--chart-type', '-ct', type=click.Choice(['line']), required=required,
                default='line', help='Graph type.')(f)

        return decorator

    @staticmethod
    def chart_name_option(required=False):
        def decorator(f):
            return click.option(
                '--chart-name', '-c', metavar='<str>', required=required,
                help='The name of the chart. The name is used in order to identify the chart against different '
                     'experiments and through the same experiment.')(f)

        return decorator

    @staticmethod
    def chart_x_option(required=False):
        def decorator(f):
            return click.option(
                '--chart-x', '-cx', metavar='<json_string>', required=required,
                help='Array of m data points (X axis), Can be Strings, Integers or Floats.')(f)

        return decorator

    @staticmethod
    def chart_y_option(required=False):
        def decorator(f):
            return click.option(
                '--chart-y', '-cy', metavar='<json_string>', required=required,
                help='Array/Matrix of m data values. Can be either array m of Integers/Floats or a matrix (m arrays having n Ints/Floats each),  a full matrix describing the values of every chart in every data point')(f)

        return decorator

    @staticmethod
    def chart_y_name_option(required=False):
        def decorator(f):
            return click.option(
                '--chart-y-name', '-cyn', metavar='<json_str>', required=required, default='Y',
                help='Display name for chart(s) Y axis')(f)

        return decorator

    @staticmethod
    def chart_x_name_option(required=False):
        def decorator(f):
            return click.option(
                '--chart-x-name', '-cxn', metavar='<str>', required=required, default='X',
                help='Display name for charts X axis')(f)

        return decorator


class ExperimentsOptions(object):
    @staticmethod
    def metrics_option(required=False):
        def decorator(f):
            return click.option(
                '--metrics', '-m', metavar='<json_string>', required=required,
                help='The metrics of the experiment as a jsonified string. The key should be the metric '
                     'name with "ex" prefix e.g. "ex_cost". The value is the metric value in String, Float, '
                     'Integer or Boolean.')(f)

        return decorator

    @staticmethod
    def model_weights_hash_option(required=False):
        def decorator(f):
            return click.option(
                '--weights-hash', '-wh', metavar='<sha1_hex>', required=required,
                help="The hexadecimal sha1 hash of the model's weights")(f)

        return decorator
