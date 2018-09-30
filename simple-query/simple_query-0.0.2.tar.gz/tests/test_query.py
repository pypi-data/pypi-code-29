from unittest import TestCase
from operator import eq, gt

from simple_query.query import Query, Matcher, Field, Criteria


class QueryAllTests(TestCase):

    def test_with_no_items(self):
        items = []
        query = Query(items)
        self.assertEqual(query.all(), items)

    def test_with_some_items(self):
        items = ['One', 'Two', 'Three']
        query = Query(items)
        self.assertEqual(query.all(), items)


class Person:
    def __init__(self, last_name):
        self.last_name = last_name


class QueryFilterTests(TestCase):

    def test_with_no_items(self):
        people = []
        filtered = Query(people).filter('last_name', eq, 'Fowler')
        self.assertEqual(filtered.all(), [])

    def test_with_no_matching_items(self):
        people = [Person(last_name='Hopper')]
        filtered = Query(people).filter('last_name', eq, 'Fowler')
        self.assertEqual(filtered.all(), [])

    def test_with_only_matching_items(self):
        people = [
            Person(last_name='Fowler'), Person(last_name='Fowler'),
            Person(last_name='Fowler')]
        filtered = Query(people).filter('last_name', eq, 'Fowler')
        self.assertEqual(filtered.all(), people)

    def test_with_only_one_matching_item(self):
        people = [
            Person(last_name='Hopper'), Person(last_name='Fowler'),
            Person(last_name='Lovelace')]
        filtered = Query(people).filter('last_name', eq, 'Fowler')
        self.assertEqual(filtered.all(), people[1:2])

    def test_with_different_operator(self):
        people = [Person(last_name='Hopper')]
        filtered = Query(people).filter('last_name', gt, 'Fowler')
        self.assertEqual(filtered.all(), people)


class CriteriaTests(TestCase):

    def test_matches(self):
        criteria = Criteria('last_name', eq, 'Fowler')
        self.assertTrue(criteria.includes(Person('Fowler')))

    def test_does_not_match(self):
        criteria = Criteria('last_name', eq, 'Fowler')
        self.assertFalse(criteria.includes(Person('Hopper')))

    def test_other_operator(self):
        criteria = Criteria('last_name', gt, 'Fowler')
        self.assertTrue(criteria.includes(Person('Hopper')))


class MatcherTests(TestCase):

    def test_does_not_match(self):
        matcher = Matcher(eq, 'Fowler')
        self.assertFalse(matcher.matches('Hopper'))

    def test_does_match(self):
        matcher = Matcher(eq, 'Fowler')
        self.assertTrue(matcher.matches('Fowler'))

    def test_other_operator(self):
        matcher = Matcher(gt, 'Fowler')
        self.assertTrue(matcher.matches('Hopper'))


class FieldTests(TestCase):

    def test_get(self):
        person = Person(last_name='Hopper')
        self.assertEqual(person.last_name, Field('last_name').get_for(person))
