# gridslice
# command-line tool for slicing your images
# Copyright (C) 2018 jack01

import argparse, sys, os
from PIL import Image

pil_read_write_types = ('.png', '.tiff', '.tif', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.webp')

# Clamp/constrain since python doesnt have one
def clamp(n, min, max):
    return max(min(max, n), min)

def main():
    parser = argparse.ArgumentParser(description='Command line tool for slicing an image on a grid.',)
    parser.add_argument('inputImagePath', help = 'Path to the input image file')
    parser.add_argument('startX', type = int, help = 'Start x')
    parser.add_argument('startY', type = int, help = 'Start y')
    parser.add_argument('width', type = int, help = 'Slice width')
    parser.add_argument('height', type = int, help = 'Slice height')
    parser.add_argument('slicesX', type = int, help = 'Number of x slices')
    parser.add_argument('slicesY', type = int, help = 'Number of y slices')

    args = parser.parse_args()

    if args.inputImagePath.lower().endswith(pil_read_write_types) == False:
        print('error: the specified output image file is not in a supported format')
        sys.exit(1)

    try:
        image = Image.open(args.inputImagePath)
    except:
        print('error: there was an error opening the image file')
        sys.exit(1)

    count = 0
    extension = os.path.splitext(args.inputImagePath)[1]

    for y in range(args.startY, args.startY + args.height * (args.slicesY), args.height):
        for x in range(args.starX, args.startX + args.width * (args.slicesX), args.width):
            slice = image.crop((x, y, x + args.width, y + args.height))

            filename = os.path.splitext(args.inputImagePath)[0] + " slice " + str(count)

            existingCount = 0
            while os.path.isfile(filename + extension):
                filename += "-" + str(existingCount)
                existingCount += 1

            try:
                slice.save(filename + extension, quality = 100)
            except:
                print('error: there was an error saving the image file ' + filename + extension)
                sys.exit(1)

            count += 1
