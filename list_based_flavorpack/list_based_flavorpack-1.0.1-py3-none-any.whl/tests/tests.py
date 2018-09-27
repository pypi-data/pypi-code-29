from django.test import TestCase
from quartet_templates.models import Template
from list_based_flavorpack.models import ListBasedRegion, ProcessingParameters
from django.core.management import call_command
from serialbox import models as sb_models
from quartet_output.models import EndPoint, AuthenticationInfo
from quartet_capture.models import Rule, Step
from quartet_templates.models import Template


class TemplateTest(TestCase):
    '''
    Tests the Template model.
    '''
    def create_template(self, name: str, content: str, description: str):
        return Template.objects.create(name=name, content=content, description=description)

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
        self.assertTrue(isinstance(template, Template))

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


class ListBasedRegionTest(TestCase):
    '''
    Tests the creation of a list-based region.
    '''
    def test_list_based_region_creation(self):
        content = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:bla:bla">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:SpecialXML>
         <RequestSize>{{ allocate.size }}</RequestSize>
      </urn:SpecialXML>
   </soapenv:Body>
</soapenv:Envelope>
        '''
        template =  Template.objects.create(name="test template", content=content, description="A test template")
        list_based_region = ListBasedRegion()
        list_based_region.template = template
        list_based_region.processing_class_path = "list_based_flavorpack.processing_classes.third_party_processing.processing.ThirdPartyProcessingClass"
        list_based_region.directory_path = "/tmp"
        list_based_region.number_replenishment_size = 20
        list_based_region.save()
        self.assertEqual("/tmp/" + str(list_based_region.file_id), list_based_region.file_path)
