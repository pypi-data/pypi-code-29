import string


def simple_encode(num, alphabet):
    """Encode a positive number in Base X
    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]

    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return "".join(arr)


def simple_decode(string, alphabet):
    """Decode a Base X encoded string into the number
    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = strlen - (idx + 1)
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


def encode(
    num, left=string.digits, right=string.ascii_uppercase, left_digit=2, right_digit=2
):
    assert left_digit + right_digit > 0

    if num == 0:
        return left[0] * left_digit + right[0] * right_digit

    left_max = len(left) ** left_digit
    right_max = len(right) ** right_digit
    total_max = left_max * right_max
    if num >= total_max:
        raise Exception("number {} is bigger than {}".format(num, total_max))

    left_value, right_value = divmod(num, right_max)

    left_string = simple_encode(left_value, left)
    right_string = simple_encode(right_value, right)

    if len(left_string) < left_digit:
        left_string = left[0] * (left_digit - len(left_string)) + left_string
    if len(right_string) < right_digit:
        right_string = right[0] * (right_digit - len(right_string)) + right_string

    if left_digit == 0:
        left_string = ""
    if right_digit == 0:
        right_string = ""

    return left_string + right_string


def decode(
    string,
    left=string.digits,
    right=string.ascii_uppercase,
    left_digit=2,
    right_digit=2,
):
    assert len(string) == left_digit + right_digit, string
    right_max = len(right) ** right_digit
    left_value = simple_decode(string[:left_digit], left)
    right_value = simple_decode(string[left_digit:], right)

    return left_value * right_max + right_value


def test():
    s = set()
    for x in range(10000):
        c = encode(x)
        assert c not in s, s
        s.add(c)
        o = decode(c)
        assert o == x, "{} == {}".format(o, x)
    print(s)
