import StringIO


def tobits(s):
    result = []

    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])

    return result


def images_to_gif(images):
    tmp = StringIO.StringIO()

    return images[0].save(
        tmp,
        format='gif',
        save_all=True,
        append_images=images[1:],
        duration=100,
        loop=0
    ), tmp
