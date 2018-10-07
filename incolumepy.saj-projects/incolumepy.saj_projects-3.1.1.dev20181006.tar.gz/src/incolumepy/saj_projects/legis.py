#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = "@britodfbr"
__copyright__ = "Copyright 2007, incolume.com.br"
__credits__ = ["Ricardo Brito do Nascimento"]
__license__ = "GPL"
__version__ = "1.0a"
__maintainer__ = "@britodfbr"
__email__ = "contato@incolume.com.br"
__status__ = "Production"


import re
import os
import locale
import platform
import json
import numpy as np
import pandas as pd
from inspect import stack
from bs4 import BeautifulSoup
from bs4 import Doctype
from bs4 import Comment
from datetime import datetime as dt
from os.path import abspath, join, isfile
from unicodedata import normalize


def locate_parent(**kwargs):
    '''

    :param kwargs: soup and tag_name both strings
    :return: bs4 with element finded
    '''
    if kwargs.get('soup').name == kwargs.get('tag_name'):
        return kwargs.get('soup')
    locate_parent(soup=kwargs.get('soup').parent,
                  tag_name=kwargs.get('tag_name'))

def change_parent(**kwargs):
    ''''''
    if kwargs.get('soup').name == kwargs.get('tag_name'):
        kwargs.get('soup').name = kwargs.get('new_tag_name')
        return kwargs.get('soup')
    change_parent(soup=kwargs.get('soup').parent,
                  tag_name=kwargs.get('tag_name'),
                  new_tag_name=kwargs.get('new_tag_name'))


def check_parent(**kwargs):
    '''
    :param kwargs: soup, tag_name, key, value
    :return: soup with setted <tag_name key="value" />
    '''

    if kwargs.get('soup').name == kwargs.get('tag_name'):
        kwargs.get('soup')[kwargs.get('key')] = kwargs.get('value')
        return kwargs.get('soup')
    check_parent(soup=kwargs.get('soup').parent,
                 tag_name=kwargs.get('tag_name'),
                 key=kwargs.get('key'), value=kwargs.get('value'))


def presidente_identify(soup, json_file, content=''):
    '''Identifica o presidente no soup recebido'''
    if not soup and content:
        soup = BeautifulSoup(content, 'html5lib')

    with open(abspath(json_file)) as jf:
        presidentes = json.load(jf)


    for item in presidentes['presidentes'].values():
        #print(item)
        for i in [x for x in item['nome'].split() if len(x) > 2]:
            #print(i)
            result = soup.find_all(string=re.compile(i, re.I), limit=10)
            if result:
                p = result[0].replace('.', '')
                #print(p)
                if set([x.lower() for x in p.split() if len(x)>2]).issubset(set(item['nome'].lower().split())):
                    return result
    return False


def governo_ano(json_file, ano=dt.today().strftime('%Y')):
    '''recebe o ano do governo e retorna str com o nome do presidente'''
    # print(ano)
    with open(os.path.abspath(json_file)) as jf:
        presidentes = json.load(jf)

    # print(presidentes)
    for item in presidentes['presidentes'].values():
        # print(item['imandato'], item['fmandato'])
        if dt.strptime(item['imandato'], "%d de %B de %Y") < dt.strptime(ano, "%Y") < dt.strptime(item['fmandato'], "%d de %B de %Y"):
            #print(item['nome'])
            return item['nome'].upper()

    return False


def presidente_em_exercicio(soup, json_file, content=''):
    '''identifica o nome do presidente em exercício'''
    if not soup and content:
        soup = BeautifulSoup(content, 'html5lib')

    with open(abspath(json_file)) as jf:
        presidentes = json.load(jf)

    vices =[]

    for item in presidentes['presidentes'].values():
        # print(item)
        for i in [x for x in item['nome'].split() if len(x) > 2]:
            # print(i)
            result = soup.find_all(string=re.compile(i, re.I), limit=10)
            if result:
                p = result[0].replace('.', '')
                # print(p)
                if set([x.lower() for x in p.split() if len(x) > 2]).issubset(set(item['nome'].lower().split())):
                    return result
        if isinstance(item['vice'], str):
            vices.append(item['vice'])
        elif isinstance(item['vice'], list):
            vices += item['vice']

    for vice in vices:
        for i in [x for x in vice.split() if len(x) > 2]:
                result = soup.find_all(string=re.compile(i, re.I), limit=10)
                if result:
                    p = result[0].replace('.', '')
                    if set([x.lower() for x in p.split() if len(x) > 2]).issubset(set(vice.lower().split())):
                        return result
    return False


def loc_presidente_exercicio(soup, presidentes_file=abspath(join('..', '..', 'data', 'presidente_exercicio.csv'))):
    '''

    :param soup:
    :param presidentes_file:
    :return:
    '''
    # logger.debug('Inicio de {}'.format(stack()[0][3]))
    presidentes_file = abspath(presidentes_file)
    assert isfile(presidentes_file), "Arquivo {} não disponível.".format(presidentes_file)
    assert isinstance(soup, BeautifulSoup), '"soup" deverá ser instancia de bs4.BeautifulSoup'
    df = pd.read_csv(presidentes_file)

    sf0 = pd.concat([df.nome.str.strip().dropna(), df.vice.str.strip().dropna()]).str.upper()
    sf = sf0[~sf0.str.contains('NONE')]
    #for i, j in enumerate(sf):
    #    print(i, j)

    result = pd.Series(np.sort(sf.str.strip().unique()))
    #for i, j in enumerate(result):
    #    print(i, j)
    munus3 = lambda s: normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')
    for i, presidente in enumerate(result):
        # logger.info('Presidente em exercício: #{:4} {}'.format(i, presidente))
        for j in [x for x in presidente.split() if len(x)>3]:
            # print(j)
            queries = soup.find_all(string=re.compile(j, re.I), limit=1)
            if queries:
                # logger.debug(queries)
                # logger.info('>> Conteúdo de queries: {}'.format(queries[-1].strip()))
                # logger.warning('>> {}'.format(set(queries[-1].strip().upper().split())))
                if set([munus3(x).upper() for x in queries[-1].strip().replace('.','').split()]
                       ).issubset([munus3(x) for x in presidente.split()]):
                    # logger.info('Presidente localizado: {}'.format(queries[-1].strip()))
                    return queries

    # logger.info('Presidente não localizado')
    # logger.debug('Finalização de {}'.format(stack()[0][3]))
    return False


def loc_ministro(soup, referenda='../../data/referendas.csv'):
    '''
    Localiza o ministro pelo nome dentro do soup fornecido.
    :param soup: Objeto SOUP
    :param referenda: lista com o nome de ministros
    :return: Lista com todos os ministros identificados no Ato
    '''

    if not isinstance(soup, BeautifulSoup):
        raise TypeError('Not is Beautfulsoap')

    # logger.debug('Inicio de {}'.format(stack()[0][3]))
    dataframe = pd.read_csv(abspath(referenda), encoding='iso8859-1',
                            names=['sigla', 'orgao', 'titular', 'interino', 'posse', 'afastamento'], header=0)
    sf = pd.concat([dataframe.titular.str.strip().dropna(), dataframe.interino.str.strip().dropna()])

    sf = sf[~sf.str.contains('\*|um dos', regex=True, case=False)]
    munus1 = lambda s: re.sub('\)', '', string=s).strip()
    munus2 = lambda s: s.split('(')[-1]
    munus3 = lambda s: normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')
    referenda = set()
    df = pd.DataFrame(sf)
    df['1'] = sf.apply(munus1).apply(munus2).apply(munus3)
    df.columns = ["old", "new"]
    result = pd.Series(np.sort(df.new.str.strip().unique()))

    for i, ministro in enumerate(result):
        # logger.info('Ministro #{:4}: {}'.format(i, ministro))
        for j in [x for x in ministro.split() if len(x)>3]:
            result = soup.find_all(string=re.compile(j, re.I), limit=20)
            if result:
                # logger.debug(result)
                for nome in result:
                    # logger.info('>> Conteúdo de Result: {}'.format(nome))
                    if set([munus3(x).upper() for x in
                            nome.replace('.','').split()]).issubset([x for x in ministro.split()]):
                        referenda.add(nome.strip())
    if referenda:
        # logger.debug('Ministro Localizado: {}'.format(referenda))
        # logger.debug('Finalização de {}'.format(stack()[0][3]))
        return referenda

    # logger.warning('Ministro não encontrado.')
    # logger.debug('Finalização de {}'.format(stack()[0][3]))
    return False


def vice_identify(json_file, ano=dt.today().strftime('%Y')):
    '''recebe o ano do governo e retorna str com o nome do vice-presidente'''
    ano = str(ano)
    # print(ano)
    if platform.system() == 'Linux':
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    else:
        locale.setlocale(locale.LC_ALL, 'pt_BR')

    with open(abspath(json_file)) as jf:
        presidentes = json.load(jf)

    # print(presidentes)
    for item in presidentes['presidentes'].values():
        # print(item['imandato'], item['fmandato'])
        if dt.strptime(item['imandato'], "%d de %B de %Y") < dt.strptime(ano, "%Y") < dt.strptime(item['fmandato'],
            "%d de %B de %Y"):
            print(f"presidente: {item['nome']}\nvice: {item['vice']}")
            return item['vice'].upper().strip()

    return False


class Legis:
    def __init__(self, **kwargs):
        self.soup = None
        self.file = None
        self.urls = []
        self.date = None
        for item, value in kwargs.items():
            self.__dict__[item] = value



    def link_css(self, **kwargs):
        '''

        :param kwargs: url
        :return: soup with tag link of type css
        '''
        urls=["http://www.planalto.gov.br/ccivil_03/css/legis_3.css",
              "https://www.planalto.gov.br/ccivil_03/css/legis_3.css"]
        # urls.append('../../../css/legis_3.css')

        if 'url' in kwargs:
            urls.append(kwargs['url'])

        soup = BeautifulSoup('', 'html.parser')
        for item in urls:
            soup.append(soup.new_tag('link', type="text/css", rel="stylesheet", href=item))
        return soup


    def charset(self, **kwargs):
        ''''''
        soup = BeautifulSoup('', 'lxml')
        tag = soup.new_tag('meta')
        tag2 = soup.new_tag('meta')
        tag3 = soup.new_tag('meta')
        try:
            tag['content'] = 'text/html; charset={}'.format(kwargs['charset'])
            tag2['charset'] = kwargs['charset']
        except:
            tag['content'] = 'text/html; charset=UTF-8'
            tag2['charset'] = 'UTF-8'
        finally:
            tag['http-equiv'] = "Content-Type"
            tag3['http-equiv'] = "Content-Language"
            tag3['content'] = "pt-br"
            soup.append(tag3)
            soup.append(tag)
            soup.append(tag2)

        return soup


    def meta(self, **kwargs):
        itens = {'numero': None, 'tipo': 'decreto', 'ano': dt.today().strftime('%Y'),
            'situacao': "vigente ou revogado", 'origem': 'Poder Executivo', 'chefe_de_governo': '',
            'referenda': '','correlacao': '', 'veto': '', 'dataassinatura': '',"generator_user": "@britodfbr",
            'publisher': 'Centro de Estudos Jurídicos da Presidência da República',
            "Copyright": 'PORTARIA Nº 1.492 DE 5/10/2011. http://www.planalto.gov.br/ccivil_03/Portaria/P1492-11-ccivil.htm',
            'fonte': '', 'presidente_em_exercicio': '', 'vice_presidente': '',
            'revised': dt.today().strftime('%Y-%m-%d %X %z'),
            'description': 'Atos Normativos Federais do Governo Brasileiro',
            'keywords':'', 'robots': 'index, nofollow', 'googlebot': 'index, follow',
            'generator': 'Centro de Estudos Juridicos (CEJ/SAJ/CC/PR)',
            'reviewer': ''
        }
        soup = BeautifulSoup('', 'html.parser')

        for key, value in itens.items():
            tag = soup.new_tag('meta')
            tag['content'] = value
            tag['name'] = key
            soup.append(tag)

        return soup


    def nav(self):
        '''
        <nav>
        <ul>
        <li>
           <a class="show-action" href="#">Texto completo</a>
           <a class="hide-action" href="#view">Texto original</a>
        </li>
        <li><a class="textoimpressao" href="#textoimpressao">Texto para impressão</a></li>
        <li><a href="#">Vide Recurso extraordinário nº 522897</a></li>
        </ul>
        </nav>
        :return:
        '''

        soup = BeautifulSoup('', 'lxml')
        soup.append(soup.new_tag('nav'))
        soup.nav.append(soup.new_tag('ul'))

        a = soup.new_tag('a', **{'href': "#view", 'class': "hide-action"})
        a.string = 'Texto compilado'


        a1 = soup.new_tag('a', **{'href': "#", 'class': "show-action"})
        a1.string = 'Texto original'


        li = soup.new_tag('li')
        li.append(a)
        li.append(a1)
        soup.nav.ul.append(li)

        a2 = soup.new_tag('a', **{'href': "#textoimpressao", 'class': "textoimpressao"})
        a2.string = 'Texto para impressão'
        li = soup.new_tag('li')
        li.append(a2)
        soup.nav.ul.append(li)

        a3 = soup.new_tag('a', href='#')
        a3.string = 'Vide Recurso extraordinário'
        li = soup.new_tag('li')
        li.append(a3)
        soup.nav.ul.append(li)

        # soup.nav.ul.append(soup.new_tag('li'))
        # soup.nav.ul.li.next_sibling.append(a2)
        # soup.nav.ul.insert(0, soup.new_tag('li'))
        # soup.nav.ul.li.append(a3)

        return soup


    def baseurl(self, **kwargs):
        soup = BeautifulSoup('', 'lxml')
        if 'target' not in kwargs:
            kwargs['target'] = '_self'
        if 'href' not in kwargs:
            raise ValueError('href nao definido')
        soup.append(soup.new_tag('base', target=kwargs['target'], href=kwargs['href']))
        return soup


    def header(self, **kwargs):
        '''  <header>
        <h1>
        Presidência da República
        </h1>
        <h2>
        Casa Civil
        </h2>
        <h3>
        Subchefia para Assuntos Jurídicos
        </h3>
        </header>'''
        if not kwargs:
            kwargs['h1'] = 'Presidência da República'
            kwargs['h2'] = 'Casa Civil'
            kwargs['h3'] = 'Subchefia para Assuntos Jurídicos'

        soup = BeautifulSoup('', 'lxml')
        soup.append(soup.new_tag('header'))
        soup.header.append(soup.new_tag('h1'))
        soup.header.append(soup.new_tag('h2'))
        soup.header.append(soup.new_tag('h3'))
        soup.header.h1.string = kwargs['h1']
        soup.header.h2.string = kwargs['h2']
        soup.header.h3.string = kwargs['h3']
        return soup


    def doctype(self, text='', default='html5'):
        DTD={'html5':'html',
            'html_401s':'HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"',
            'html_401t': 'HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"',
            'html_401f':'HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd"',
            'xhtml_11': 'html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"',
            'xhtml_10f': 'html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd"',
            'xhtml_10t': 'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"',
            'xhtml_10s': 'html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"'
             }
        if not text:
            text = DTD[default]
        tag = Doctype(text)
        return tag


    def comment(self, text):
        tag = Comment(text)
        return tag


    def dou(self, text=None):
        soup = BeautifulSoup('', 'lxml')
        tag = soup.new_tag('p')
        tag['class'] = "dou"
        tag.string = 'Este texto não substitui o publicado no D.O.U.'
        if text:
            tag['string'] = text
        return tag

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        if value:
            self._file = os.path.abspath(value)

    def get_soup_from_file(self, parser_index=0):
        parser = ["html.parser", 'lxml', 'lxml-xml', 'xml', 'html5lib']
        if not self._file:
            raise ValueError('self.file not defined')
        try:
            f = open(self._file).read()
        except:
            f = open(self._file, encoding='iso8859-1').read()

        self.soup = BeautifulSoup(f, parser[parser_index])
        return self.soup


    def replace_brastra(self, img=None, index=0):
        img_l=['http://www.planalto.gov.br/ccivil_03/img/Brastra.gif',
             'http://www.planalto.gov.br/ccivil_03/img/Brastra.png',
             'http://www.planalto.gov.br/ccivil_03/img/Brastra01.png',
             'http://www.planalto.gov.br/ccivil_03/img/brasaorep.png'
             ]
        logo = self.soup.select('img[src*="Brastra"]')
        if img:
            logo[0]['src'] = img
        else:
            logo[0]['src'] = img_l[index]
        return True, logo

    @classmethod
    def date_conv(cls, date):
        ''' convert date to timestamp
                :param date: ' de 8 de Janeiro de 1900'
                :return: 1900/1/8
        '''
        if platform.system() == 'Linux':
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        else:
            locale.setlocale(locale.LC_ALL, 'pt_BR')

        date = date.lower().replace('.', '').strip()

        try:
            return dt.strptime(date, 'de %d de %B de %Y').strftime('%Y/%m/%d')
        except ValueError:
            return dt.strptime(date, 'de %dº de %B de %Y').strftime('%Y/%m/%d')

    def set_date(self):
        tag = self.soup.select('p[class="epigrafe"]')[0].text.strip()
        epigrafe = re.split('[,–.-]', tag)
        if epigrafe[-1]:
            self.date = self.date_conv(epigrafe[-1])
        else:
            self.date = self.date_conv(epigrafe[-2])
        return self.date


def run():
    a = Legis()
    print(type(a.link_css()))
    print((a.link_css().prettify()))

    print('*'*20)
    print(type(a.meta(numero=1234)))
    print(a.meta(numero=1234).prettify())
    print('*'*20)
    print(a.header().prettify())
    print('*'*20)
    print(a.nav().prettify())
    print('*'*20)
    print(a.baseurl(href='http://www.planalto.gov.br/ccivil_03/', target='_blank'))
    print('*' * 20)

    print(a.doctype())
    print(type(a.comment('Comentario de teste.')))

    print('*' * 20)
    a.file = '../../../CCIVIL_03/decreto/1980-1989/1985-1987/D95578.htm'
    print(a.file)
    print('*' * 20)
    print(a.get_soup_from_file())
    print('*' * 20)
    print(a.replace_brastra('http://www.planalto.gov.br/ccivil_03/img/Brastra.png'))
    print(a.soup)

    print('*' * 20)
    a.file = '../../../CCIVIL_03/decreto/D3630.htm'
    (a.get_soup_from_file())
    print(a.replace_brastra())
    print(a.soup)

    print(a.date_conv(' DE 8 DE MAIO DE 2018'))
    print(a.dou())
    print(a.meta(charset='UTF-8'))
    print(type(a.doctype()), a.doctype())

    soup = BeautifulSoup('<html><body></body></html>', 'html.parser')
    soup.insert(0, a.doctype(default='xhtml_11'))
    soup.body.append(a.comment("It's a comment!"))
    print(soup.prettify())

    soup = BeautifulSoup('<html><head></head><body></body></html>', 'html.parser')
    soup.insert(0, a.doctype())
    print(soup.prettify())

    soup = BeautifulSoup('', 'lxml')
    soup.append(a.baseurl(href='http://www.planalto.gov.br/ccivil_03'))
    print(soup.prettify())

    print(a.nav().prettify())

    print(a.charset())


if __name__ == '__main__':
    run()
