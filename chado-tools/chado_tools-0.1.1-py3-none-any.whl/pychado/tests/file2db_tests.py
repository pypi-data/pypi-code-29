import unittest
from pychado import utils
from pychado.io import load_ontology


class TestFile2Db(unittest.TestCase):
    """Tests"""

    def test_filter_results(self):
        john = utils.EmptyObject(name="John")
        mike = utils.EmptyObject(name="Mike")
        persons = [john, mike]
        filtered_persons = load_ontology.filter_objects(persons, name="Mike")
        self.assertEqual(len(filtered_persons), 1)
        self.assertEqual(filtered_persons[0], mike)
        with self.assertRaises(AttributeError):
            load_ontology.filter_objects(persons, age=42)
            
    def test_list_to_dict(self):
        john = utils.EmptyObject(name="John")
        mike = utils.EmptyObject(name="Mike")
        persons = [john, mike]
        persons_dict = load_ontology.list_to_dict(persons, "name")
        self.assertEqual(len(persons_dict), 2)
        self.assertIn("John", persons_dict)
        self.assertEqual(persons_dict["John"], john)
        with self.assertRaises(AttributeError):
            load_ontology.list_to_dict(persons, "age")

    def test_split_dbxref(self):
        result = load_ontology.split_dbxref("testdb:testaccession:testversion")
        self.assertEqual(result[0], "testdb")
        self.assertEqual(result[1], "testaccession")
        self.assertEqual(result[2], "testversion")

        result = load_ontology.split_dbxref("testdb:testaccession")
        self.assertEqual(result[0], "testdb")
        self.assertEqual(result[1], "testaccession")
        self.assertEqual(result[2], "")

        with self.assertRaises(AttributeError):
            load_ontology.split_dbxref("testdb_testaccession")

    def test_create_dbxref(self):
        result = load_ontology.create_dbxref("testdb", "testaccession", "testversion")
        self.assertEqual(result, "testdb:testaccession:testversion")

        result = load_ontology.create_dbxref("testdb", "testaccession")
        self.assertEqual(result, "testdb:testaccession")

        with self.assertRaises(AttributeError):
            load_ontology.create_dbxref("testdb", "")


if __name__ == '__main__':
    unittest.main(verbosity=2, buffer=True)
