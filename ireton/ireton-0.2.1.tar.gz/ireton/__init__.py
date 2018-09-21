import inspect

IRETON_FIXTURES = dict()


def require(check, err_message):
    if not check:
        raise ValueError(err_message)


def parametrize(test_values):
    def parametrize_decorator(func):
        signature = inspect.signature(func)
        require(len(test_values) > 0, 'require at least one test value')
        input_sizes = set(map(len, test_values))
        require(len(input_sizes) == 1, 'inputs\'s size should be homogeneous')
        input_size = input_sizes.pop()
        require(input_size == len(signature.parameters),
                f'provided inputs of size {input_size} but '
                f'the test takes {len(signature.parameters)} args')
        errors = []
        out = None
        for test_value in test_values:
            try:
                out = func(*test_value)
            except AssertionError as e:
                e.args = tuple(list(e.args) + [f'Failed on: {test_value}'])
                errors.append(e)
        if len(errors) != 0:
            raise AssertionError("\n" + "\n".join(map(str, errors)))
        return out

    return parametrize_decorator


def use_session_fixture():
    def with_fixture_decorator(func):
        signature = inspect.signature(func)
        param_names = signature.parameters.keys()
        fixture_names = set(param_names)
        available_fixtures = set(IRETON_FIXTURES.keys())
        require(len(signature.parameters) > 0, 'require at least one fixture name as an argument')
        require(fixture_names.issubset(available_fixtures),
                f'cloudn\'t find these fixtures: '
                ", ".join(fixture_names.difference(available_fixtures)))
        fixtures = list(map(IRETON_FIXTURES.get, param_names))
        out = func(*fixtures)
        return out

    return with_fixture_decorator


def define_session_fixture():
    def define_fixture_decorator(func):
        fixture_name = func.__name__
        global IRETON_FIXTURES
        IRETON_FIXTURES[fixture_name] = func() # TODO: recursively use fixtures
    return define_fixture_decorator
