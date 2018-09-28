from callpass import Callpass


def test_correctness():
    assert Callpass("ab2def") == 17826
    assert Callpass("xyzmb2") == 13252


def test_instance_comparison():
    a = Callpass("ab2def")
    b = Callpass("xyzmb2")
    assert a == a
    assert b == b
    assert a != b
    assert b != a


def test_int_comparison():
    callpass = Callpass("12345")
    assert callpass == 17636
    assert callpass != 0


def test_str_comparison():
    callpass = Callpass("12345")
    assert callpass == "17636"
    assert callpass != "0"


def test_zeros_padding():
    assert Callpass("a&!") == "05060"
    assert Callpass("a+%!") == "06120"
