#coding: utf-8
from bs4 import BeautifulSoup
import re
import os
from incolumepy.utils.files import realfilename
from unicodedata import normalize
from inspect import stack


def limpar_planalto(conteudo):
    ''''''
    # logger.debug('{} Iniciado..'.format(stack()[0][3]))
    a = Clean_html()
    a.conteudo = conteudo
    # print(a.conteudo)
    a.clean()
    soup = BeautifulSoup(a.conteudo, 'html.parser')

    #Remove header title
    if soup.table:
        soup.table.decompose()
    conteudo = re.sub('<br[\ /]*>', '</p><p>', str(soup), flags=re.MULTILINE)
    conteudo = re.sub('<sup>\s*o\s*</sup>', 'º ', conteudo, flags=re.MULTILINE)
    conteudo = re.sub('<strike>\s*º\s*</strike>', 'º ', conteudo, flags=re.MULTILINE)
    soup = BeautifulSoup(conteudo, 'html5lib')

    # logger.debug('{} Finalizado com sucesso..'.format(stack()[0][3]))
    return soup.prettify()


def remover_acentos(self, txt):
    ''' Remove acentos de caracteres não ascii
    :param txt: string
    :return: string sem caracteres especiais

    >>> self.remover_acentos('áàãâäÁÀÃÂÄ! éèêëÉÈẼÊË? íìîïÍÌĨÎÏ, óòõôöÓÒÕÔÖ; úùûüÚÙŨÛÜ.')
    aaaaaAAAAA! eeeeEEEEE? iiiiIIIII, oooooOOOOO; uuuuUUUUU.
    '''
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


class Clean_html:
    TXT = '[ACENTUAÇÃO] açaí: áàãâäÁÀÃÂÄ! éèêëÉÈẼÊË? íìîïÍÌĨÎÏ, óòõôöÓÒÕÔÖ; úùûüÚÙŨÛÜ.'

    def __init__(self):
        self.file = None
        self.data = []
        self.conteudo = None
        self.filename = None
        self.path = None

    @classmethod
    def remover_acentos(self, txt):
        ''' Remove acentos de caracteres não ascii
        :param txt: string
        :return: string sem caracteres especiais

        >>> self.remover_acentos('áàãâäÁÀÃÂÄ! éèêëÉÈẼÊË? íìîïÍÌĨÎÏ, óòõôöÓÒÕÔÖ; úùûüÚÙŨÛÜ.')
        aaaaaAAAAA! eeeeEEEEE? iiiiIIIII, oooooOOOOO; uuuuUUUUU.
        '''
        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    def get_file_content(self):
        try:
            with open(self.file) as file:
                self.data.append(file.read())
                self.path = os.path.dirname(file.name)
                self.filename = os.path.basename(file.name)
        except:
            with open(self.file, encoding='iso8859-1') as file:
                self.data.append(file.read())
                self.path = os.path.dirname(file.name)
                self.filename = os.path.basename(file.name)


    def clean(self):
        try:
            if not self.conteudo:
                self.get_file_content()

            if not self.data:
                self.data.append(self.conteudo)

            #print(self.conteudo)
            #print(type(self.data[0]))
            #print(re.sub('&nbsp;|\n', ' ', self.data[0]))


            self.data.append(re.sub('&nbsp;|\n', ' ', str(BeautifulSoup(self.data[0], 'html5lib')), flags=re.MULTILINE))
            self.data[1] = re.sub('\s+', ' ', self.data[1], flags=re.MULTILINE)
            self.data[1] = re.sub('<sup>\s?o\s?</sup>', 'º ', self.data[1], flags=re.MULTILINE)
            self.data[1] = re.sub('<sup>\s?a\s?</sup>', 'ª ', self.data[1], flags=re.MULTILINE)
            soup = BeautifulSoup(self.data[-1], 'html.parser')

            # remover tags e seu conteudo
            tag = []
            tag.append('meta[name="GENERATOR"]')
            tag.append('link[rel*="STYLESHEET"]')
            tag.append('style')
            for j in tag:
                container = soup.select(j)
                for a, i in enumerate(container):
                    # print(a, i.parent)
                    i.decompose()

            ## desatachar tags
            #print('\n' * 3)
            tag = []
            tag.append('big')
            tag.append('u')
            tag.append('font')
            tag.append('span')
            tag.append('strong')
            tag.append('small')
            tag.append('html')
            tag.append('body')
            for j in tag:
                container = soup.select(j)
                for i in container:
                    i.unwrap()

            # attrs remove
            # print('\n'*3)
            tag = []
            tag.append('xmlns')
            tag.append('bgcolor')
            tag.append('align')
            tag.append('style')
            tag.append('width')
            for i in tag:
                container = soup.select('[{}]'.format(i))
                for j in container:
                    del j[i]

            # remove classes MS
            container = soup.select('[class*="Ms"]')
            for i in container:
                del i['class']

            # adding str html e body
            soup = BeautifulSoup('<html><body>{}</body></html>'.format(str(soup)), 'html.parser')

            # wrap body
            tag = soup.new_tag('body')
            #soup.new_tag('body').wrap(soup)
            #tag.append(soup)

            #for item in soup.find_all():
            #    tag.append(item.extract())
            #soup = tag

            # wrap html
            #soup.wrap(soup.new_tag('html'))
            #container = soup.find_parents('head')
            #print(container)

            # Realocar head
            soup.html.insert(0, soup.body.head.extract())

            self.conteudo = soup.prettify()
            #print(soup.prettify())
        except IOError:
            raise

    def write(self):
        os.rename(os.path.join(self.path, self.filename), realfilename(os.path.join(self.path, self.filename)))
        with open(realfilename(os.path.join(self.path, self.filename)), 'w') as file:
            file.write(self.conteudo)
        return True


    @staticmethod
    def run(file='../file.html'):
        a = Clean_html()
        try:
            assert os.path.isfile(file)
            a.file = file
        except AssertionError:
            a.file = '../../testes/file.html'

        a.clean()
        print(a.__dict__)
        print(a.filename)
        print(a.write())
        print(a.remover_acentos(a.TXT))
        print(Clean_html.remover_acentos(Clean_html.TXT))


if __name__ == '__main__':
    Clean_html.run()
