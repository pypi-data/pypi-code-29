import numpy as np

def overlay(size, count, sources, color=(255, 255, 255)):
    '''
    Create a sequence of frames by overlaying the sources
    onto a blank background
    '''
    for i in range(count):
        background = np.empty((size[1], size[0], 3), dtype=np.uint8)
        background[:, :] = color
        for source, pos in sources:
            frame = next(source)
            background[pos[1]:pos[1]+frame.shape[1],
                       pos[0]:pos[0]+frame.shape[0]] = frame
        yield background
        

