import time
import uuid
import re
import codecs
from . import file_templates
from .. import utils


class ManifestGenerator(object):

    def __init__(self, target_filepath, book_name, author, publisher, images, xhtmls):
        self.target_filepath = target_filepath
        self.book_name = book_name
        self.author = author
        self.publisher = publisher
        self.images = images
        self.xhtmls = xhtmls

    def generate(self):
        image_items, xhtml_items, itemrefs = self.gen_file_manifest()
        utils.mkfile(self.target_filepath, file_templates.manifest_template.format(
            book_name=self.book_name,
            author=self.author,
            publisher=self.publisher,
            uuid=uuid.uuid1(),
            time=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime()),
            images=image_items,
            xhtmls=xhtml_items,
            itemrefs=itemrefs,
        ))

    def gen_file_manifest(self):
        # Images
        image_items = ''
        for i in range(0, len(self.images)):
            if i == 0:
                image_item = file_templates.cover_image_item.format(suffix=self.images[i].suffix)
            else:
                image_item = file_templates.image_item.format(
                    id=self.images[i].id,
                    image_filename=self.images[i].moved_name,
                    suffix=self.images[i].suffix,
                )
            image_items += image_item
        
        # xhtmls
        xhtml_items = ''
        for i in range(0, len(self.xhtmls)):
            if i == 0:
                xhtml_item = file_templates.cover_xhtml_item
            else:
                xhtml_item = file_templates.xhtml_item.format(
                    xhtml_id=self.xhtmls[i].id,
                    xhtml_filename=self.xhtmls[i].filename,
                    image_id=self.images[i].id,
                )
            xhtml_items += xhtml_item
        
        # Itemrefs
        itemrefs = ''
        for i in range(0, len(self.images)):
            if i == 0:
                itemref = file_templates.cover_itemref
            else:
                if i % 2 == 1:
                    itemref = file_templates.right_itemref.format(
                        id=self.xhtmls[i].id
                    )
                else:
                    itemref = file_templates.left_itemref.format(
                        id=self.xhtmls[i].id
                    )
            itemrefs += itemref

        return image_items, xhtml_items, itemrefs