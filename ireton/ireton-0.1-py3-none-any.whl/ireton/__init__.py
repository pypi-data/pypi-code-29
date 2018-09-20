import functools
import inspect


def require(check, err_message):
    if not check:
        raise ValueError(err_message)

def parametrize(test_values):
    def parametrize_decorator(func):
        arg_spec = inspect.signature(func)
        require(len(test_values) > 0, 'require at least one test value')
        input_sizes = set(map(len, test_values))
        require(len(input_sizes) == 1, 'inputs\'s size should be homogeneous')
        input_size = input_sizes.pop()
        require(input_size == len(arg_spec.parameters),
                f'provided inputs of size {input_size} but '
                f'the test takes {len(arg_spec.parameters)} args')
        errors = []
        for test_value in test_values:
            try:
                func(*test_value)
            except AssertionError as e:
                e.args = tuple(list(e.args) + [f'Failed on: {test_value}'])
                errors.append(e)
        if len(errors) != 0:
            raise AssertionError("\n" + "\n".join(map(str, errors)))
        return func
    return parametrize_decorator

