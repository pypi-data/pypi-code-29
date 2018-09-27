import re
import os
import codecs
from . import file_templates
import eroepub.utils as utils

class XhtmlInfo(object):
    
    def __init__(self):
        self.filename = ''
        self.id = ''

    def set_id(self):
        self.id = re.search(r"[^\.]+", self.filename).group(0)

class XhtmlGenerator(object):

    def __init__(self, target_dir_path, images, book_name):
        self.target_dir_path = target_dir_path
        self.images = images
        self.book_name = book_name
        self.xhtmls = []

    def generate(self):
        for i in range(0, len(self.images)):
            if i == 0:
                xhtml_name = 'p_cover.xhtml'
            else:
                xhtml_name = "p_{:0>4d}.xhtml".format(i - 1)
            xhtml_path = os.path.join(self.target_dir_path, xhtml_name)
            utils.mkfile(xhtml_path, file_templates.xhtml_template.format(
                book_name=self.book_name,
                image_filename=self.images[i].moved_name,
                width=self.images[i].width,
                height=self.images[i].height,
            ))
            xhtml_info = XhtmlInfo()
            xhtml_info.filename = xhtml_name
            xhtml_info.set_id()
            self.xhtmls.append(xhtml_info)

    def get_xhtmls(self):
        return self.xhtmls