from behave import *
import sys
import tempfile
import lib
from mock import patch
from mock import *

from io import StringIO
from lib import stats
from lib import diff
from lib import norm
from lib import merge

use_step_matcher("parse")


@given("the file {} containing")
def step_impl(context, file_name):
    """
    :type context: behave.runner.Context
    """
    text = context.text  # .replace(" ", "\t")

    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.write(bytes(text, 'UTF-8'))
    tf.close()

    setattr(context, file_name, tf.name)
    # context.tmp_files.append(tf.name)


@given("the parameter {} with the file argument {}")
def step_impl(context, param, file_name):
    """
    :type context: behave.runner.Context
    sample_cli
    """
    sys.argv.append(param)
    sys.argv.append(getattr(context, file_name))


@given("the parameter {} with the string argument {}")
def step_impl(context, param, file_name):
    """
    :type context: behave.runner.Context
    sample_cli
    """
    sys.argv.append(" ".join([param, file_name]))
    # sys.argv.append(getattr(context, file_name))


@when("we run {} from stats")
def step_impl(context, function):
    """
    :param function:
    :type context: behave.runner.Context
    """

    # print(context.__dict__)
    # with patch.object(ParseVectors, 'parse') as mock_method:
    #    mock_method.return_value = context.matrix

    result = getattr(stats, function)(context.parser)

    #fobj = lib.operations_dict["Stats"][function]
    #result = fobj(context)
    #print("@@@")
    # stats.sample(function_name)
    # module = getattr(module_name)
    # print(module)
    # function = getattr(module_name, function_name)
    # print(function)
    # result = getattr(function)(context)


@then("we expect the output")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    output = context.stdout_capture.getvalue().rstrip()
    command_output = output.strip()
    print(command_output)
    context_test = context.text.strip()
    print(context_test)

    assert command_output == context_test




