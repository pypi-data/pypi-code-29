def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

Black = rgb_to_hex((0,0,0))
White = rgb_to_hex((255,255,255))
Green = rgb_to_hex((0,255,0))
Blue = rgb_to_hex((0,0,255))
Red = rgb_to_hex((255,0,0))
Yellow = rgb_to_hex((255,255,0))
Magenta = rgb_to_hex((255,0,255))
Cyan = rgb_to_hex((0,255,255))
