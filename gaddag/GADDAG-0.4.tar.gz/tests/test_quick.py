import os

import pytest

@pytest.fixture()
def gaddag():
    import gaddag
    return gaddag

def test_order_adding_words(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "guz"])
    gdg2 = gaddag.GADDAG(["guz", "foo", "bar"])

    assert(gdg1 == gdg2)

def test_order_adding_prefix(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "foobar"])
    gdg2 = gaddag.GADDAG(["foobar", "foo"])

    assert(gdg1 == gdg2)

def test_order_adding_suffix(gaddag):
    gdg1 = gaddag.GADDAG(["bar", "foobar"])
    gdg2 = gaddag.GADDAG(["foobar", "bar"])

    assert(gdg1 == gdg2)

def test_len(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    assert(len(gdg1) == 4)

def test_has_word(gaddag):
    gdg1 = gaddag.GADDAG(["foo"])
    assert("foo" in gdg1)

def test_has_word_prefix(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "foobar"])
    assert("foo" in gdg1 and "foobar" in gdg1)

def test_has_word_suffix(gaddag):
    gdg1 = gaddag.GADDAG(["bar", "foobar"])
    assert("bar" in gdg1 and "foobar" in gdg1)

def test_not_has_word_empty(gaddag):
    gdg1 = gaddag.GADDAG()
    assert(not "foo" in gdg1)

def test_not_has_word(gaddag):
    gdg1 = gaddag.GADDAG(["bar"])
    assert(not "foo" in gdg1)

def test_not_has_word_suffix(gaddag):
    gdg1 = gaddag.GADDAG(["foobar"])
    assert(not "bar" in gdg1)

def test_not_has_word_prefix(gaddag):
    gdg1 = gaddag.GADDAG(["foobar"])
    assert(not "foo" in gdg1)

def test_iter_words(gaddag):
    words = {"foo", "bar", "baz", "foobar"}
    gdg1 = gaddag.GADDAG(words)
    result = {word for word in gdg1}

    assert(result == words)

def test_iter_words_duplicates(gaddag):
    words = ["foo", "bar", "baz", "foobar"]
    gdg1 = gaddag.GADDAG(words)
    result = [word for word in gdg1]

    assert(len(result) == len(words))

def test_equal_empty(gaddag):
    gdg1 = gaddag.GADDAG()
    gdg2 = gaddag.GADDAG()

    assert(gdg1 == gdg2)

def test_equal_words(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    gdg2 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])

    assert(gdg1 == gdg2)

def test_unequal_words(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    gdg2 = gaddag.GADDAG(["foo", "bar"])

    assert(gdg1 != gdg2)

def test_root(gaddag):
    gdg1 = gaddag.GADDAG()
    assert(gdg1.root == gaddag.Node(gdg1.gdg, 0))

def test_contains(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    result = {word for word in gdg1.contains("oo")}
    expected = {"foo", "foobar"}

    assert(result == expected)

def test_contains_duplicates(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    result = [word for word in gdg1.contains("o")]

    assert(len(result) == 2)

def test_starts_with(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    result = {word for word in gdg1.starts_with("fo")}
    expected = {"foo", "foobar"}

    assert(result == expected)

def test_starts_with_duplicates(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    result = [word for word in gdg1.starts_with("fo")]

    assert(len(result) == 2)

def test_starts_with_empty(gaddag):
    gdg1 = gaddag.GADDAG()
    result = {word for word in gdg1.starts_with("fo")}
    expected = set()

    assert(result == expected)

def test_ends_with(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    result = {word for word in gdg1.ends_with("ar")}
    expected = {"bar", "foobar"}

    assert(result == expected)

def test_ends_with_duplicates(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    result = [word for word in gdg1.ends_with("ar")]

    assert(len(result) == 2)

def test_ends_with_empty(gaddag):
    gdg1 = gaddag.GADDAG()
    result = {word for word in gdg1.ends_with("ar")}
    expected = set()

    assert(result == expected)

def test_follow(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "baz", "foobar"])
    expected = gdg1.root["o"]["o"]["f"]

    assert(gdg1.root.follow("oof") == expected)

def test_follow_raises_keyerror(gaddag):
    gdg1 = gaddag.GADDAG(["foo", "bar", "foobar"])

    with pytest.raises(KeyError):
        gdg1.root.follow("baz")

def test_save_load(gaddag):
    gdg_path = os.path.join(os.path.dirname(__file__), "test.gdg")

    gdg1 = gaddag.GADDAG(["foo", "bar", "foobar"])
    gdg1.save(gdg_path, compressed=False)
    gdg2 = gaddag.load(gdg_path)

    os.remove(gdg_path)
    assert(gdg1 == gdg2)

def test_save_load_compressed(gaddag):
    gdg_path = os.path.join(os.path.dirname(__file__), "test.gdg")

    gdg1 = gaddag.GADDAG(["foo", "bar", "foobar"])
    gdg1.save(gdg_path)
    gdg2 = gaddag.load(gdg_path)

    os.remove(gdg_path)
    assert(gdg1 == gdg2)

