from unittest import TestCase, main
from incolumepy.saj_projects import legis
from incolumepy.saj_projects.legis import BeautifulSoup


class TestLegis(TestCase):
    def setUp(self):
        self.leg = legis.Legis()
        self.soup1 = BeautifulSoup('<div><p><b><i>teste</i></b></p></div>', 'html5lib')

    def test_instance(self):
        self.assertTrue(isinstance(legis.Legis, self.leg))

    def test_link(self):
        esperado = '<link href="http://www.planalto.gov.br/ccivil_03/css/legis_3.css" rel="stylesheet" type="text/css"/>'
        esperado += '<link href="https://www.planalto.gov.br/ccivil_03/css/legis_3.css" rel="stylesheet" type="text/css"/>'
        self.assertEqual(esperado, self.leg.link_css())

    def test_header(self):
        h = '<header><h1>Presidência da República</h1><h2>Casa Civil</h2><h3>Subchefia para Assuntos Jurídicos</h3></header>'
        self.assertEqual(h, self.leg.header())

    def test_baseUrl(self):
        result = '<base href="http://www.planalto.gov.br/ccivil_03/" target="_blank"/>'
        self.assertEqual(result, self.leg.baseurl(href='http://www.planalto.gov.br/ccivil_03/', target='_blank'))

    def test_nav(self):
        result = '<nav><ul><li><a class="hide-action" href="#view">Texto compilado</a><a class="show-action" href="#">Texto original</a></li><li><a class="textoimpressao" href="#textoimpressao">Texto para impressão</a></li><li><a href="#">Vide Recurso extraordinário</a></li></ul></nav>'
        self.assertEqual(result, self.leg.nav())

    def test_comentario(self):
        from incolumepy.saj_projects.legis import Comment
        result1 = 'Comentario de teste.'
        op = self.leg.comment('Comentario de teste.')
        self.assertEqual(Comment, type(op))
        self.assertEqual(result1, op)

    def test_doctype(self):
        from incolumepy.saj_projects.legis import Doctype

        self.assertEqual(Doctype, type(self.leg.doctype()))

        self.assertEqual('html', self.leg.doctype())

        self.assertEqual('html', self.leg.doctype(default='html5'))

        r1 = 'HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"'
        self.assertEqual(r1, self.leg.doctype(default='html_401s'))
        self.assertEqual(r1, self.leg.doctype(r1))

        r2 = 'HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"'
        self.assertEqual(r2, self.leg.doctype(default='html_401t'))
        self.assertEqual(r2, self.leg.doctype(r2))

        r3 = 'HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd"'
        self.assertEqual(r3, self.leg.doctype(default='html_401f'))
        self.assertEqual(r3, self.leg.doctype(r3))

        r4 = 'html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"'
        self.assertEqual(r4, self.leg.doctype(default='xhtml_11'))
        self.assertEqual(r4, self.leg.doctype(r4))

        r5 = 'html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd"'
        self.assertEqual(r5, self.leg.doctype(default='xhtml_10f'))
        self.assertEqual(r5, self.leg.doctype(r5))

        r6 = 'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"'
        self.assertEqual(r6, self.leg.doctype(default='xhtml_10t'))
        self.assertEqual(r6, self.leg.doctype(r6))

        r7 = 'html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"'
        self.assertEqual(r7, self.leg.doctype(default='xhtml_10s'))
        self.assertEqual(r7, self.leg.doctype(r7))

    def test_date_conv(self):
        self.assertEqual('2018/05/08', self.leg.date_conv(' DE 8 DE MAIO DE 2018'))
        self.assertEqual('2018/06/01', self.leg.date_conv(' DE 1º DE JUNHO DE 2018'))
        self.assertEqual('2018/12/01', self.leg.date_conv(' DE 1º DE dezembro DE 2018'))

    def test_date_conv_raises(self):
        self.assertRaises(ValueError, self.leg.date_conv(' de 29 de fevereiro de 1900'))

    def test_dou(self):
        r1 = '<p class="dou">Este texto não substitui o publicado no D.O.U.</p>'
        self.assertEqual(r1, self.leg.dou())

    def test_locate_parent(self):
        q = self.soup1.find_all('teste')
        result = legis.locate_parent(soup=q, tag_name='div')
        self.assertEqual('div', result.parent.name)

    def test_change_parent(self):
        q = self.soup1.find_all('teste')
        result = legis.change_parent(soup=q, tag_name='div', new_tag_name='blockquote')
        self.assertEqual('blockquote', result.parent.name)

    def test_check_parent(self):
        q = self.soup1.find_all('teste')
        result = legis.check_parent(soup=q, tag_name='p', key='id', value='date')
        self.assertEqual('date', self.soup1.p['id'])

    def test_presidente_identify(self):
        raise NotImplementedError

    def test_governo_ano(self):
        raise NotImplementedError

    def test_presidente_em_exercicio(self):
        pass

    def test_loc_presidente_exercicio(self):
        pass

    def test_loc_ministro(self):
        pass

    def test_vice_identify(self):
        pass


if __name__ == '__main__':
    main()
