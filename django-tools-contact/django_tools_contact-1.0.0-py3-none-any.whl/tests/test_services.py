from django.test import TestCase, override_settings
from djtools.contact import services
from djtools.contact.models import ContactRequest, ContactInformation


class ServicesTestCase(TestCase):
    def test_send_mail(self):
        contact_request = ContactRequest.objects.create()
        amount_sent_emails = services._send_mail(contact_request)
        self.assertEqual(amount_sent_emails, 1)

    def test_create_contact_request(self):
        contact_request, amount_sent_emails = services.create_contact_request(
            name="test",
            email="test@example.com",
            phone_number="555-123",
            message="Test"
        )
        self.assertEqual(contact_request.name, "test")
        self.assertEqual(amount_sent_emails, 1)

    @override_settings(DJTOOLS_CONTACT_INFO=True)
    def test_get_contact_information(self):
        old_contact_information = ContactInformation.objects.create(
            longitude=1.1,
            latitude=0.0
        )
        new_contact_information = services.get_contact_information()
        self.assertEqual(old_contact_information, new_contact_information)

    def test_get_contact_information_dissabled(self):
        self.assertIsNone(services.get_contact_information())
