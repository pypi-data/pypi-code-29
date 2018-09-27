from django.test import TestCase
from quartet_templates import models

class TemplateTest(TestCase):
    '''
    Tests the Template model.
    '''
    def create_template(self, name: str, content: str, description: str):
        return models.Template.objects.create(name=name, content=content, description=description)

    def test_template_creation(self):
        content = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:bla:bla">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:SpecialXML>
         <SomethingSpecial>{{ something_special }}</SomethingSpecial>
      </urn:SpecialXML>
   </soapenv:Body>
</soapenv:Envelope>
        '''
        template = self.create_template(name="Test Template", content=content, description="A Test Template")
        self.assertTrue(isinstance(template, models.Template))

    def test_template_rendering(self):
        content = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:bla:bla">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:SpecialXML>
         <SomethingSpecial>{{ something_special }}</SomethingSpecial>
      </urn:SpecialXML>
   </soapenv:Body>
</soapenv:Envelope>
        '''
        template = self.create_template(name="Test Template", content=content, description="A Test Template")
        rendered = template.render(context={"something_special": "Special Value"})
        expected = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:bla:bla">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:SpecialXML>
         <SomethingSpecial>Special Value</SomethingSpecial>
      </urn:SpecialXML>
   </soapenv:Body>
</soapenv:Envelope>
        '''
        self.assertEqual(expected, rendered)
