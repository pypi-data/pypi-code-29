import sys


class CharacterLine(object):
    def __init__(
        self,
        x,
        y,
        z=0,
        layer=None,
        char="'",
        fg_color=None,
        bg_color=None
    ):
        self.layer = layer
        self.x = x
        self.y = y
        self.z = z
        self.char = char
        self.fg_color = fg_color
        self.bg_color = bg_color

    def head(self):
        c = ''

        if self.fg_color is not None:
            c = chr(27) + '[' + str(30 + self.fg_color) + 'm' + c

        if self.bg_color is not None:
            c = chr(27) + '[' + str(40 + self.bg_color) + 'm' + c

        return c

    def tail(self):
        if self.fg_color or self.bg_color:
            return chr(27) + "[0m"


class Template(object):
    def __init__(
        self,
        data,
        fg_color=None,
        bg_color=None,
        display_offset=None,
        align=('left', 'top')
    ):
        self.data = data
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.display_offset = display_offset
        self.align = align

    def stamp(
        self,
        world,
        x,
        y,
        z=0,
        layer=None,
        invisible=False
    ):
        return ConsoleObject(
            world,
            x,
            y,
            z,
            layer,
            self.data,
            self.fg_color,
            self.bg_color,
            invisible,
            self.display_offset,
            self.align
        )


class ConsoleObject(object):
    def __init__(
        self,
        world,
        x,
        y,
        z=0,
        layer=None,
        data=(",,", "`´"),
        fg_color=None,
        bg_color=None,
        invisible=False,
        display_offset=None,
        align=('left', 'top')
    ):
        self.layer = layer
        self.world = world
        self.x = x
        self.y = y
        self.z = z
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.invisible = invisible
        self.data = data

        # alignment
        box = self.bounding_box()

        if align[0].lower() == 'center':
            self.x -= int((box[1] - box[0]) / 2)

        elif align[0].lower() == 'right':
            self.x -= (box[1] - box[0])

        if align[1].lower() == 'center':
            self.y -= int((box[3] - box[2]) / 2)

        if align[1].lower() == 'bottom':
            self.y -= (box[3] - box[2])

        self.display_offset = list(display_offset or (0, 0))[:2]

        self.lines = None

        self.update()

    def hide(self):
        self.invisible = True
        self.update()

    def show(self):
        self.invisible = False
        self.update()

    def set_invisible(self, invisible):
        self.invisible = invisible
        self.update()

    def set_data(self, data):
        self.data = data
        self.update()

    def visual_offset(self, offs=(0, 0), relative=False):
        if relative:
            self.display_offset[0] += offs[0]
            self.display_offset[1] += offs[1]

        else:
            self.display_offset[0] = offs[0]
            self.display_offset[1] = offs[1]

        self.update()

    def set_color(self, fg_color=-1, bg_color=-1):
        if fg_color != -1:  # so None can be used
            self.fg_color = fg_color

        if bg_color != -1:
            self.bg_color = bg_color

        self.update()

    def bounding_box(self, include_offset=False):
        x1 = None
        y1 = None
        x2 = None
        y2 = None

        for y, line in enumerate(self.data if type(self.data) is not str else self.data.split('\n')):
            for x, c in enumerate(line):
                if c != ' ' or self.bg_color is not None:
                    if x1 is None or x < x1:
                        x1 = x

                    if x2 is None or x > x2:
                        x2 = x

                    if y1 is None or y < y1:
                        y1 = y

                    if y2 is None or y > y2:
                        y2 = y

        if x1 is None:
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0

        elif include_offset:
            x1 += self.display_offset[0]
            x2 += self.display_offset[0]
            y1 += self.display_offset[1]
            y2 += self.display_offset[1]

        return (x1 + self.x, x2 + self.x, y1 + self.y, y2 + self.y)

    def update(self):
        if self.lines is not None:
            self.world.remove(*self.lines)

        if type(self.data) is str:
            self.lines = [CharacterLine(
                self.x + self.display_offset[0],
                self.y + i + self.display_offset[1],
                self.z,
                self.layer,
                d,
                self.fg_color,
                self.bg_color
            ) for i, d in enumerate(self.data.split('\n'))]

        else:
            self.lines = [CharacterLine(
                self.x + self.display_offset[0],
                self.y + i + self.display_offset[1],
                self.z,
                self.layer,
                d,
                self.fg_color,
                self.bg_color
            ) for i, d in enumerate(self.data)]

        if not self.invisible:
            self.world.add(*self.lines)

    def move(self, dx=None, dy=None, dz=None, relative=True):
        if relative:
            self.x += dx or 0
            self.y += dy or 0
            self.z += dz or 0

        else:
            if dx is not None:
                self.x = dx

            if dy is not None:
                self.y = dy

            if dz is not None:
                self.z = dz

        self.update()

    def set_layer(self, new_layer):
        self.layer = new_layer
        self.update()


class CameraObject(ConsoleObject):
    def update(self):
        super().update()

        self.world.set_camera(self.x, self.y, self.z)


class RectObject(ConsoleObject):
    def __init__(
        self,
        world,
        x,
        y,
        width,
        height,
        stroke_char='@',
        fill_char='@',
        z=0,
        layer=None,
        fg_color=None,
        bg_color=None,
        invisible=False,
        display_offset=None
    ):
        self.layer = layer
        self.world = world
        self.x = x
        self.y = y
        self.width = abs(width)
        self.height = abs(height)
        self.z = z
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.invisible = invisible
        self.stroke_char = stroke_char
        self.fill_char = fill_char
        self.display_offset = list(display_offset or (0, 0))[:2]

        self.lines = None
        self.update()

    def bounding_box(self, include_offset=False):
        x1 = self.x
        x2 = self.x + self.width
        y1 = self.y
        y2 = self.y + self.height

        if include_offset:
            x1 += self.display_offset[0]
            x2 += self.display_offset[0]
            y1 += self.display_offset[1]
            y2 += self.display_offset[1]

        return (x1, x2, y1, y2)

    def update(self):
        self.data = '\n'.join(self.line_data())
        super().update()

    def line_data(self):
        return (
            [self.stroke_char * self.width] + (
                [self.stroke_char + (
                    self.fill_char * (self.width - 2)
                ) + self.stroke_char] * (self.height - 2)
            ) + [self.stroke_char * self.width]
        )


class World(object):
    def __init__(
        self,
        width=90,
        height=32,
        cam_x=0,
        cam_y=0,
        cam_z=0,
        objects=(),
        current_layer=None,
        frame=None
    ):
        self.current_layer = current_layer
        self.objects = list(objects)
        self.width = width
        self.height = height
        self.cam_x = cam_x
        self.cam_y = cam_y
        self.cam_z = cam_z
        self.frame = frame

    def set_camera(self, x=0, y=0, z=1):
        self.cam_x = x
        self.cam_y = y
        self.cam_z = z

    def move_camera(self, dx=0, dy=0, dz=0):
        self.cam_x += dx
        self.cam_y += dy
        self.cam_z += dz

    def remove(self, *objects):
        for o in objects:
            if o in self.objects:
                self.objects.remove(o)

    def add(self, *objects):
        self.objects.extend(objects)

    def set_layer(self, l):
        self.current_layer = l

    def render(self):
        data = []
        object_map = {}

        if self.frame is not None:
            data.append(
                self.frame[0] +
                self.frame[1] * self.width +
                self.frame[0]
            )

        for o in self.objects:
            depth = (
                1 + o.z - self.cam_z
            )

            if depth < 0.02:
                continue

            eff_y = int(
                (o.y - self.cam_y) * depth + self.height / 2
            )

            if (
                (
                    o.layer is None or
                    (
                        self.current_layer is not None and
                        o.layer == self.current_layer
                    )
                ) and
                eff_y >= 0 and
                eff_y < self.height
            ):
                if eff_y in object_map:
                    object_map[eff_y].append(o)

                else:
                    object_map[eff_y] = [o]

        for y in range(self.height):
            if y not in object_map:
                if self.frame is not None:
                    data.append(
                        self.frame[1] +
                        ' ' * self.width +
                        self.frame[1]
                    )

                else:
                    data.append()

            else:
                line = [' '] * self.width
                z = [None] * self.width

                for obj in object_map[y]:
                    for i, c in enumerate(obj.char):
                        depth = (
                            1 + obj.z - self.cam_z
                        )

                        c_eff_x = int(
                            (obj.x + i - self.cam_x) * depth + self.width / 2
                        )

                        if (
                            (obj.head() != '' or c != ' ') and
                            c_eff_x >= 0 and
                            c_eff_x < len(line) and
                            (
                                z[c_eff_x] is None or
                                obj.z > z[c_eff_x]
                            )
                        ):
                            z[c_eff_x] = obj.z
                            line[c_eff_x] = (obj.head() or '') + \
                                c + \
                                (obj.tail() or '')

                if self.frame is not None:
                    data.append(self.frame[1] + ''.join(line) + self.frame[1])

                else:
                    data.append(''.join(line))

        if self.frame is not None:
            data.append(
                self.frame[0] +
                self.frame[1] * self.width +
                self.frame[0]
            )

        sys.stdout.write(chr(27) + '[2J' + '\n'.join(data))  # "VSync"?
