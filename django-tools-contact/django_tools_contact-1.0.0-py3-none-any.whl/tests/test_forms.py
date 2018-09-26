import os

from django.test import TestCase

from djtools.contact.forms import ContactRequestForm


class ContactRequestFormTestCase(TestCase):
    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'

    def test_clean(self):
        form = ContactRequestForm({
            'name': "Test",
            'message': "Test",
            'email': "test@example.com",
            'phone_number': "555-123",
            'recaptcha_response_field': 'PASSED'
        })
        self.assertTrue(form.is_valid())

    def test_clean_missing_phone(self):
        form = ContactRequestForm({
            'name': "Test",
            'message': "Test",
            'email': "test@example.com",
            'recaptcha_response_field': 'PASSED'
        })
        self.assertTrue(form.is_valid())

    def test_clean_phone_and_email(self):
        form = ContactRequestForm({
            'name': "Test",
            'message': "Test",
            'recaptcha_response_field': 'PASSED'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'__all__': ["El email o el teléfono son obligatorios."]}
        )

    def tearDown(self):
        del os.environ['RECAPTCHA_TESTING']
