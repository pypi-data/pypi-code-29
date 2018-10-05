
tests_dict = {'hello': 'hellox', 'world': 'worldw', 1: 1}


def test_hello(expect):
    for k, v in tests_dict.items():
        expect(k == v, '%s not equal %s' % (k, v))
