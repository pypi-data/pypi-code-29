import unittest
from unittest.mock import patch
from econt import api
from econt.status_codes import StatusCode
from tests.credentials import USERNAME, PASSWORD

VALID_CD_AGREEMENT_XML = '''
<response>
<is_valid>1</is_valid>
</response>
'''
INVALID_CD_AGREEMENT_XML = '''
<response>
<is_valid>0</is_valid>
</response>
'''


class CDAgreementTests(unittest.TestCase):
    def setUp(self):
        self.testing_instance = api.Econt(USERNAME, PASSWORD)

    def test_given_correct_name_correct_cd_number_expect_1(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = VALID_CD_AGREEMENT_XML
            tester = self.testing_instance.validate_cd_agreement(
                               'Ангел Антонов Данаилов', 'CD38791')
            self.assertEqual(tester. get('status'), StatusCode.STATUS_OK)
            self.assertEqual(tester.get('message'), 'OK')
            self.assertEqual(tester.get('data').get('is_valid'), '1')

    def test_given_wrong_cd_number_expect_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = INVALID_CD_AGREEMENT_XML
            tester = self.testing_instance.validate_cd_agreement(
                               'Ангел Антонов Данаилов', 'CD8791')
            self.assertEqual(tester. get('status'), StatusCode.STATUS_OK)
            self.assertEqual(tester.get('message'), 'OK')
            self.assertEqual(tester.get('data').get('is_valid'), '0')

    def test_given_no_name_expect_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = INVALID_CD_AGREEMENT_XML
            tester = self.testing_instance.validate_cd_agreement(
                               '', 'CD38791')
            self.assertEqual(tester. get('status'), StatusCode.STATUS_OK)
            self.assertEqual(tester.get('message'), 'OK')
            self.assertEqual(tester.get('data').get('is_valid'), '0')

    def test_given_no_name_no_cd_number_expect_0(self):
        with patch('requests.sessions.Session.post') as mock_post:
            mock_post.return_value.text = INVALID_CD_AGREEMENT_XML
            tester = self.testing_instance.validate_cd_agreement('', '')
            self.assertEqual(tester. get('status'), StatusCode.STATUS_OK)
            self.assertEqual(tester.get('message'), 'OK')
            self.assertEqual(tester.get('data').get('is_valid'), '0')
