import re
import os
import shutil
from PIL import Image


class ImageInfo(object):

    def __init__(self):
        self.filename = ''
        self.filepath = ''
        self.width = 0
        self.height = 0
        self.moved_name = ''
        self.suffix = ''
        self.id = ''


class ImagesProcessor(object):

    def __init__(self, dir_path, target_dir_path):
        self.images_dir_path = dir_path
        self.target_dir_path = target_dir_path
        self.images = []

    def proceed(self):
        self.scan_images()
        self.copy_images()

    def scan_images(self):
        files = os.walk(self.images_dir_path).__next__()[2]
        for name in files:
            filepath = os.path.join(self.images_dir_path, name)
            im = Image.open(filepath)
            w, h = im.size
            
            im_info = ImageInfo()
            im_info.filename = name
            im_info.filepath = filepath
            im_info.width = w
            im_info.height = h
            im_info.suffix = self.get_suffix(filepath)
            self.images.append(im_info)
    
    def get_suffix(self, filepath):
        suffix = re.search(r"(?<=\.)[^\.]+$", filepath).group(0)
        if suffix == 'jpg':
            suffix = 'jpeg'
        return suffix
    
    def copy_images(self):
        for i in range(0, len(self.images)):
            image_path = self.images[i].filepath
            if i == 0:
                moved_name = f"cover.{self.images[i].suffix}"
            else:
                moved_name = "i_{:0>4d}.{}".format(i - 1, self.images[i].suffix)
            new_path = os.path.join(
                self.target_dir_path,
                moved_name,
            )
            self.images[i].moved_name = moved_name
            self.images[i].id = re.search(r"[^\.]+", moved_name).group(0)

            shutil.copyfile(image_path, new_path)
        
    def get_images_list(self):
        return self.images