
import unittest
from adsmsg import msg

from adsmsg.augmentrecord import AugmentAffiliationRequestRecord, AugmentAffiliationResponseRecord, AugmentAffiliationRequestRecordList, AugmentAffiliationResponseRecordList

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_affiliation_request(self):
        d = {'bibcode': '2003ASPC..295..361M',
                  'status': 2,
                  'affiliation': 'University of Deleware',
                  'author': 'Stephen McDonald',
                  'sequence': '1/2'}
        a = AugmentAffiliationRequestRecord(**d)
        self.assertEqual(a.bibcode, d['bibcode'])
        self.assertEqual(a.status, d['status'])
        self.assertEqual(a.affiliation, d['affiliation'])
        self.assertEqual(a.author, d['author'])
        self.assertEqual(a.sequence, d['sequence'])

    def test_affiliation_request_list(self):
        d_list = [{'bibcode': '2003ASPC..295..361M',
                   'status': 2,
                   'affiliation': 'University of Deleware',
                   'author': 'Stephen McDonald',
                   'sequence': '1/2'},
                  {'bibcode': '2003ASPC..295..361Z',
                  'status': 2,
                  'affiliation': 'University of Zeleware',
                  'author': 'Ztephen McDonald',
                  'sequence': '2/2'}]
        m = AugmentAffiliationRequestRecordList()
        m.status = 2
        for r in d_list:
            m.affiliation_requests.add(**r)
        for i in range(len(d_list)):
            self.assertEqual(m.affiliation_requests[i].bibcode, d_list[i]['bibcode'])
            self.assertEqual(m.affiliation_requests[i].status, d_list[i]['status'])
            self.assertEqual(m.affiliation_requests[i].affiliation, d_list[i]['affiliation'])
            self.assertEqual(m.affiliation_requests[i].author, d_list[i]['author'])
            self.assertEqual(m.affiliation_requests[i].sequence, d_list[i]['sequence'])


    def test_affiliation_response(self):
        d = {'bibcode': '2003ASPC..295..361M',
             'status': 2,
             'affiliation': 'University of Deleware',
             'author': 'Stephen McDonald',
             'sequence': '1/2',
             'canonical_affiliation': 'U of D',
             'canonical_affiliation_id': '1'}
        a = AugmentAffiliationResponseRecord(**d)
        self.assertEqual(a.bibcode, d['bibcode'])
        self.assertEqual(a.status, d['status'])
        self.assertEqual(a.affiliation, d['affiliation'])
        self.assertEqual(a.author, d['author'])
        self.assertEqual(a.sequence, d['sequence'])
        self.assertEqual(a.canonical_affiliation, d['canonical_affiliation'])
        self.assertEqual(a.canonical_affiliation_id, d['canonical_affiliation_id'])        
    def test_affiliation_response_list(self):
        d_list = [{'bibcode': '2003ASPC..295..361M',
                   'status': 2,
                   'affiliation': 'University of Deleware',
                   'author': 'Stephen McDonald',
                   'sequence': '1/2',
                   'canonical_affiliation': 'U of D',
                   'canonical_affiliation_id': '1'},
                  {'bibcode': '2003ASPC..295..361Z',
                   'status': 2,
                   'affiliation': 'University of Zeleware',
                   'author': 'Ztephen McDonald',
                   'sequence': '2/2',
                   'canonical_affiliation': 'U of Z',
                   'canonical_affiliation_id': '2'}]
        m = AugmentAffiliationResponseRecordList()
        m.status = 2
        for r in d_list:
            m.affiliation_responses.add(**r)
        for i in range(len(d_list)):
            self.assertEqual(m.affiliation_responses[i].bibcode, d_list[i]['bibcode'])
            self.assertEqual(m.affiliation_responses[i].status, d_list[i]['status'])
            self.assertEqual(m.affiliation_responses[i].affiliation, d_list[i]['affiliation'])
            self.assertEqual(m.affiliation_responses[i].author, d_list[i]['author'])
            self.assertEqual(m.affiliation_responses[i].sequence, d_list[i]['sequence'])
            self.assertEqual(m.affiliation_responses[i].canonical_affiliation, d_list[i]['canonical_affiliation'])
            self.assertEqual(m.affiliation_responses[i].canonical_affiliation_id, d_list[i]['canonical_affiliation_id'])
            
