from PIL import Image
import os
import imageio

def save_gif(filename, frames, delay, loop=0):
    images = list(frames)
    imageio.mimsave(filename, images, duration=delay)

def save_png_frames(folder, base, frames, zeros=5):
    for i, frame in enumerate(frames):
        image = Image.fromarray(frame)
        image.save(os.path.join(folder, base + str(i).zfill(zeros) + '.png'))

#
# Save the first frame as a single png image
#
def save_png(filename, frames):
    image = Image.fromarray(next(frames))
    image.save(filename)
