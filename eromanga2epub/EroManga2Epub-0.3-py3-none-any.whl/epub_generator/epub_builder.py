import codecs
import os
import re
import zipfile
import shutil
import eroepub.utils as utils
from eroepub.epub_generator import file_templates
from eroepub.epub_generator.images_processor import ImagesProcessor
from eroepub.epub_generator.manifest_generator import ManifestGenerator
from eroepub.epub_generator.xhtml_generator import XhtmlGenerator


class EpubBuilder(object):

    def __init__(self, input_path, output_path):
        self.input_path = input_path

        self.author = ''
        self.book_name = ''
        self.identify()

        self.output_root = os.path.join(output_path, self.book_name + '(output)')
        self.cwd = self.output_root

    def identify(self):
        dir_name = re.search(r"(?<=[\\/])[^\\/]+$", self.input_path).group(0)
        dir_name = dir_name.replace(' ', '')

        self.book_name = re.search(r"(?<=[\]\)])[^\[\]\(\)]+", dir_name).group(0)

        author_regex = re.findall(r"(?<=\[)[^\[\]]+(?=\])", dir_name)
        if author_regex[0].endswith('汉化组'):
            self.author = author_regex[1]
        else:
            self.author = author_regex[0]

    def cd(self, *dest):
        self.cwd = os.path.join(self.output_root, *dest)

    def make_main_structure(self):
        # Cwd is /book_name at first
        # Make main dir
        os.mkdir(self.cwd)

        self.cd('mimetype')
        utils.mkfile(self.cwd, file_templates.mimetype)
        
        self.cd('META-INF')
        os.mkdir(self.cwd)
        self.cd('META-INF', 'container.xml')
        utils.mkfile(self.cwd, file_templates.container_xml)
            
        self.cd('OEBPS')
        os.mkdir(self.cwd)
        self.cd('OEBPS', 'navigation-documents.xhtml')
        utils.mkfile(self.cwd, file_templates.navigation_documents_xhtml)

        self.cd('OEBPS', 'image')
        os.mkdir(self.cwd)
        self.cd('OEBPS', 'text')
        os.mkdir(self.cwd)
        self.cd('OEBPS', 'style')
        os.mkdir(self.cwd)
        self.cd('OEBPS', 'style', 'fixed-layout-jp.css')
        utils.mkfile(self.cwd, file_templates.fixed_layout_jp_css)

    def make_details(self):
        self.cd('OEBPS', 'image')
        pro = ImagesProcessor(self.input_path, self.cwd)
        pro.proceed()
        images = pro.get_images_list()

        self.cd('OEBPS', 'text')
        xhtml = XhtmlGenerator(self.cwd, pro.get_images_list(), self.book_name)
        xhtml.generate()
        xhtmls = xhtml.get_xhtmls()

        self.cd('OEBPS', 'standard.opf')
        mfst = ManifestGenerator(
            self.cwd,
            self.book_name,
            self.author,
            '',
            images,
            xhtmls,
        )
        mfst.generate()

    def make_epub(self):
        self.cd('')
        source_dir = self.cwd
        zip_filename = os.path.join(
            os.path.dirname(self.output_root),
            f"{self.book_name}.epub",
        )

        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            pre_len = len(os.path.dirname(source_dir))
            for parent, dirnames, filenames in os.walk(source_dir):
                for filename in filenames:
                    pathfile = os.path.join(parent, filename)
                    arcname = pathfile[pre_len:].strip(os.path.sep)
                    zipf.write(pathfile, arcname)
        
        shutil.rmtree(source_dir)

    def build(self):
        self.make_main_structure()
        self.make_details()
        self.make_epub()