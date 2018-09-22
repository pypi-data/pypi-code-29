def make_np_frames(size, count, draw):
    for i in range(count):
        frame = draw(size, count, i)
        yield(frame)
