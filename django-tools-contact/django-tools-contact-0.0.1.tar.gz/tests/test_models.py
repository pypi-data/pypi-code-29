from django.test import TestCase
from djtools.contact.models import ContactRequest


class ContactRequestTestCase(TestCase):
    def test_get_contact_information_only_phone(self):
        phone_number = "555-123"

        contact_request = ContactRequest.objects.create(phone_number=phone_number)

        self.assertEqual(contact_request.contact_information, phone_number)

    def test_get_contact_information_only_email(self):
        email = "test@test.com"

        contact_request = ContactRequest.objects.create(email=email)

        self.assertEqual(contact_request.contact_information, email)

    def test_get_contact_information_phone_and_email(self):
        phone_number = "555-123"
        email = "test@test.com"

        contact_request = ContactRequest.objects.create(
            phone_number=phone_number,
            email=email
        )

        self.assertEqual(
            contact_request.contact_information,
            "test@test.com o 555-123"
        )
