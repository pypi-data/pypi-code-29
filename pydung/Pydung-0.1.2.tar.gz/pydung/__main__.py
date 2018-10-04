import asyncio
import math
import time
import win32api
import win32con
import random

# from pydung import input, environment
from pydung import environment


def main():
    global vel_x, vel_y, vel_z, world, gravity

    # == Player Dynamics and Game Loop ==
    jump = False
    gravity = 6
    earth_gravity = 6
    col_radius = 0.5
    col_height = 0.2
    max_step_height = 0.05

    vel_x = 0
    vel_y = 0
    vel_z = 0

    header = "[ PYDUNG v0.1 ]"
    speed_mod = 1.0

    # === Object Templates ===
    # Decoration
    t_barrel = environment.Template("O")
    t_small_barrel = environment.Template("o")
    t_square_pillar = environment.Template(
        "/\\\n\\/", align=('center', 'center')
    )
    t_pillar_top = environment.Template(
        ".--.\n|..|\n|..|\n'--'", align=('center', 'center')
    )
    t_stair_block = environment.Template(
        "[¨¨¨¨¨¨¨¨¨¨¨¨¨]\n[_____________]",
        align=('center', 'bottom')
    )
    t_round_pillar = environment.Template(
        "()\n()", align=('center', 'center')
    )
    t_lamp = environment.Template(' *\n*+*\n *')

    # Floor Details
    t_floor_1 = environment.Template(".\n .")
    t_floor_2 = environment.Template(" .\n.")
    t_floor_3 = environment.Template(";")

    # === Defining the World ===
    world = environment.World(160, 40, frame="#+")

    physical_objects = []
    floors = []
    walls = []
    event_log = []

    # Floor Details
    for _ in range(60):
        x = random.randint(-70, 68)
        y = random.randint(-20, 5)

        random.choice((t_floor_1, t_floor_2)).stamp(world, x, y)

    for _ in range(16):
        x = random.randint(-70, 68)
        y = random.randint(-20, 5)

        t_floor_3.stamp(world, x, y)

    # Player
    cam = environment.CameraObject(
        world,
        0, -3, z=0.0001,
        data=".-.\n'-'",
        align=('center', 'center')
    )

    def make_pillar(st, x, y):
        for z in range(0, 8):
            physical_objects.append(st.stamp(world, x, y, z=z / 15))

        physical_objects.append(t_pillar_top.stamp(world, x, y, z=9 / 15))

    def make_barrel(st, x, y):
        for z in range(0, 4):
            physical_objects.append(st.stamp(world, x, y, z=z / 20))

    def make_wall(x, y, x2, y2, wz=0, stroke='#', fill=':'):
        for z in range(0, 25):
            w = environment.RectObject(
                world, x, y, x2 - x, y2 - y, z=wz + z / 20,
                stroke_char=stroke, fill_char=fill
            )

            walls.append(w)
            physical_objects.append(w)

    def make_floor(x, y, x2, y2, wz=0, stroke='#', fill=' '):
        f = environment.RectObject(
            world, x=x, y=y, width=x2 - x, height=y2 - y,
            z=wz,
            stroke_char=stroke, fill_char=fill
        )

        floors.append(f)
        physical_objects.append(f)

    def make_step(x, y, height=0):
        for z in range(0, height * 3):
            t = t_stair_block.stamp(world, x, y, z=z / 15)
            physical_objects.append(t)

    # Barrels
    make_barrel(t_barrel, -70, 5)
    make_barrel(t_barrel, -70, 4)
    make_barrel(t_small_barrel, -69, 4)
    make_barrel(t_small_barrel, -69, 5)
    make_barrel(t_small_barrel, -70, 3)

    # Pillars
    make_pillar(t_square_pillar, -1, 2)
    make_pillar(t_square_pillar, 4, 2)
    make_pillar(t_square_pillar, 9, 2)
    make_pillar(t_square_pillar, 14, 2)
    make_pillar(t_square_pillar, 19, 2)
    make_pillar(t_square_pillar, 24, 2)
    make_pillar(t_square_pillar, 29, 2)
    make_pillar(t_square_pillar, 34, 2)
    make_pillar(t_square_pillar, 39, 2)
    make_pillar(t_square_pillar, 44, 2)
    make_pillar(t_square_pillar, 49, 2)
    make_pillar(t_square_pillar, 54, 2)
    make_pillar(t_square_pillar, 59, 2)

    make_pillar(t_round_pillar, -10, -3)
    make_pillar(t_round_pillar, -15, -3)
    make_pillar(t_round_pillar, -15, -8)
    make_pillar(t_round_pillar, -10, -8)

    # Staircase
    make_step(-30, 0)
    make_step(-30, -1)
    make_step(-30, -2, 1)
    make_step(-30, -3, 1)
    make_step(-30, -4, 2)
    make_step(-30, -5, 2)
    make_step(-30, -6, 2)
    make_step(-30, -7, 2)

    # Scattered Lamps
    for _ in range(27):
        x = random.randint(-70, 68)
        y = random.randint(-20, 5)

        t_lamp.stamp(world, x, y, z=1.5)

    # Walls
    make_wall(-70, 6, 70, 10)
    make_wall(-70, -24, 70, -20)
    make_wall(-74, -24, -70, 10)
    make_wall(70, -24, 74, 10)

    # Floor
    make_floor(-74, -24, 74, 10)

    def check_keys(*keys):
        return any(
            win32api.GetAsyncKeyState(k)
            for k in keys
        )

    def will_collide(obj, dt, vel_x, vel_y, vel_z):
        box = obj.bounding_box()

        if (
            cam.x + (vel_x * dt) + col_radius > box[0] and
            cam.x + (vel_x * dt) - col_radius < box[1] and
            cam.y + (vel_y * dt) + col_radius > box[2] and
            cam.y + (vel_y * dt) - col_radius < box[3] and
            cam.z + (vel_z * dt) + col_height > obj.z and
            cam.z + (vel_z * dt) - col_height < obj.z
        ):
            min_x = max(cam.x - col_radius, min(box[0], cam.x + col_radius))
            max_x = min(cam.x + col_radius, max(box[1], cam.x - col_radius))
            min_y = max(cam.y - col_radius, min(box[2], cam.y + col_radius))
            max_y = min(cam.y + col_radius, max(box[3], cam.y - col_radius))

            if (
                abs(obj.z - cam.z + col_height) < max_step_height
                and vel_z <= 0
                and obj not in floors
            ):
                cam.move(
                    cam.x + math.copysign(
                        1, obj.x + (box[1] - box[0]) / 2 - cam.x
                    ) * 0.2,
                    cam.y + math.copysign(
                        1, obj.x + (box[3] - box[2]) / 2 - cam.x
                    ) * 0.2,
                    obj.z + col_height * 1.1,
                    relative=False
                )
                return False

            elif abs(min_x - max_x) < 0.01:
                if cam.x < (box[1] - box[0]) / 2:
                    return "RIGHT"

                return "LEFT"

            elif abs(min_y - max_y) < 0.01:
                if cam.y < (box[3] - box[2]) / 2:
                    return "TOP"

                return "BOTTOM"

            return 'MIDDLE'

        return False

    def collides(obj):
        box = obj.bounding_box()

        if (
            cam.x + col_radius > box[0] and
            cam.x - col_radius < box[1] and
            cam.y + col_radius > box[2] and
            cam.y - col_radius < box[3] and
            cam.z + col_height > obj.z and
            cam.z - col_height < obj.z
        ):
            min_x = max(cam.x - col_radius, min(box[0], cam.x + col_radius))
            max_x = min(cam.x + col_radius, max(box[1], cam.x - col_radius))
            min_y = max(cam.y - col_radius, min(box[2], cam.y + col_radius))
            max_y = min(cam.y + col_radius, max(box[3], cam.y - col_radius))

            if (
                abs(cam.z + col_radius - obj.z) < max_step_height
                and vel_z <= 0
                and obj not in floors
            ):
                cam.move(
                    cam.x + math.copysign(
                        1, obj.x + (box[1] - box[0]) / 2 - cam.x
                    ) * 0.2,
                    cam.y + math.copysign(
                        1, obj.x + (box[3] - box[2]) / 2 - cam.x
                    ) * 0.2,
                    obj.z + col_height * 1.1,
                    relative=False
                )
                return 'MIDDLE'

            elif abs(min_x - max_x) < 0.01:
                if cam.x < (box[1] - box[0]) / 2:
                    return "RIGHT"

                return "LEFT"

            elif abs(min_y - max_y) < 0.01:
                if cam.y < (box[3] - box[2]) / 2:
                    return "TOP"

                return "BOTTOM"

            return 'MIDDLE'

        return False

    jump_speed = 1.5

    async def render_loop():
        global jump, vel_x, vel_y, vel_z, speed_mod, floor, old_floor

        dt = 0
        floor = None
        old_floor = None

        while True:
            if check_keys(ord('R')):
                return

            elif check_keys(ord('Q')):
                exit(0)

            jump = check_keys(win32con.VK_CONTROL, win32con.VK_SPACE)

            if check_keys(ord('G')):
                gravity = 0

            else:
                gravity = earth_gravity

            t = time.time()

            world.render()
            print()
            print(' ' * int(world.width / 2 - len(header) / 2) + header)

            if floor is not None:
                cam.z -= col_height / 1.75

                if not will_collide(floor, dt, vel_x, vel_y, vel_z):
                    if (
                        old_floor is not None and
                        will_collide(old_floor, dt, vel_x, vel_y, vel_z)
                    ):
                        floor = old_floor
                        old_floor = None

                    else:
                        old_floor = floor
                        floor = None

                cam.z += col_height / 1.75

            def set_floor(o):
                global vel_x, vel_y, vel_z, floor, old_floor

                for o2 in physical_objects:
                    if (
                        o2 is not o and
                        will_collide(o2, dt, vel_x, vel_y, vel_z)
                        and o2.z > o.z
                    ):
                        return False

                old_floor = floor
                floor = o
                cam.move(dz=floor.z + col_height, relative=False)
                vel_z = 0

                return True

            dir = None

            if floor is None:
                vel_z -= gravity * dt * jump_speed
                blocked = False
                on_floor = None

                for o in physical_objects:
                    dir = will_collide(o, dt, vel_x, vel_y, vel_z)

                    if dir:
                        blocked = dir

                        if (
                            vel_z <= 0 and
                            cam.z - col_height + (vel_z * dt) <= o.z and
                            (
                                cam.z > o.z or
                                cam.z - o.z >= max_step_height
                            )
                        ):
                            on_floor = o

                if on_floor:
                    set_floor(on_floor)

                elif blocked:
                    if blocked == "TOP":
                        vel_x *= 0.8
                        vel_y *= -0.8

                    elif blocked == 'BOTTOM':
                        vel_x *= 0.8
                        vel_y *= -0.8

                    elif blocked == 'LEFT':
                        vel_x *= -0.8
                        vel_y *= 0.8

                    elif blocked == 'RIGHT':
                        vel_x *= -0.8
                        vel_y *= 0.8

                    else:
                        vel_x = 0
                        vel_y = 0

                cam.move(vel_x * dt, vel_y * dt, vel_z * dt)

            else:
                if jump:
                    vel_z = jump_speed
                    cam.move(dz=floor.z + col_height, relative=False)
                    cam.move(vel_x * dt, vel_y * dt, vel_z * dt)

                    if (
                        old_floor is not None and
                        will_collide(old_floor, dt, vel_x, vel_y, vel_z)
                    ):
                        floor = old_floor
                        old_floor = None

                    else:
                        old_floor = floor
                        floor = None

                else:
                    a_up = check_keys(win32con.VK_UP, ord('W'))
                    a_dn = check_keys(win32con.VK_DOWN, ord('S'))
                    a_lf = check_keys(win32con.VK_LEFT, ord('A'))
                    a_rt = check_keys(win32con.VK_RIGHT, ord('D'))

                    if check_keys(ord('Z')):
                        speed_mod = 2.0

                    else:
                        speed_mod = 1.0

                    if a_up:
                        vel_y += -160 * speed_mod * dt

                    if a_dn:
                        vel_y += 160 * speed_mod * dt

                    if a_lf:
                        vel_x += -160 * speed_mod * dt

                    if a_rt:
                        vel_x += 160 * speed_mod * dt

                    vel_z = 0
                    cam.z = 0

                    old_x = cam.x
                    old_y = cam.y
                    blocked = False

                    for o in physical_objects:
                        dir = False
                        dir = will_collide(o, dt, vel_x, vel_y, vel_z)

                        if dir:
                            if (
                                o is floor or
                                o.z >= cam.z + col_height or
                                o.z <= cam.z - col_height
                            ):
                                pass

                            elif o.z < cam.z - col_height + max_step_height:
                                if not set_floor(o):
                                    blocked = dir

                            else:
                                blocked = dir

                    if blocked:
                        cam.move(old_x, old_y, relative=False)

                        if blocked == "TOP":
                            vel_x *= 1.8
                            vel_y *= -1.8

                        elif blocked == 'BOTTOM':
                            vel_x *= 1.8
                            vel_y *= -1.8

                        elif blocked == 'LEFT':
                            vel_x *= -1.8
                            vel_y *= 1.8

                        elif blocked == 'RIGHT':
                            vel_x *= -1.8
                            vel_y *= 1.8

                        else:
                            vel_x = 0
                            vel_y = 0

                    else:
                        cam.move(vel_x * dt, vel_y * dt)

                    vel_x /= 2
                    vel_y /= 2

            print(
                'vx={} vy={} vz={}\nx={} y={} z={}\n'
                "floor={} old_floor={} jump={}\nblocked={}".format(
                    vel_x,
                    vel_y,
                    vel_z,
                    cam.x,
                    cam.y,
                    cam.z,
                    ("None" if floor is None else floor.bounding_box()),
                    (
                        "None"
                        if old_floor is None
                        else old_floor.bounding_box()
                    ),
                    jump,
                    blocked
                )
            )

            dt = time.time() - t

            print('\n' + '\n'.join('- ' + str(x) for x in event_log[-9:]))

            await asyncio.sleep(1 / 40)

    async def run():
        await render_loop()
        # await input_sys.run()

    asyncio.run(run())


if __name__ == "__main__":
    while True:
        main()