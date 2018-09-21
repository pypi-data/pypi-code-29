import uuid

from django.test import TransactionTestCase
from django.contrib.auth.hashers import check_password
from rest_framework.test import APIClient

from generic.exceptions import ObjectNotFoundError, ValidationError
from generic.helpers import str_to_uuid1
from tests.models import User, Object, UserObject, UserObjectPw
from generic.factories import generic_factory
from generic.validators import unique_field, validate_many
from generic.repositories import (GenericRepository, OwnershipRepository)
from generic.services import (generic_retrieve_single_service,
                              generic_retrieve_all_service,
                              generic_retrieve_all_by_owner_service,
                              generic_delete_service,
                              generic_update_service,
                              generic_create_service)


class GenericFactoryTest(TransactionTestCase):
    def test_factory(self):
        name = 'new object'
        kwargs = {'name': name}
        o = generic_factory(model_class=Object, **kwargs)
        self.assertEqual(Object, type(o))
        self.assertEqual(type(uuid.uuid1()), type(o.id))
        self.assertEqual(name, o.name)


class GenericRepositoryTest(TransactionTestCase):
    fixtures = ['init.json']

    def test_find_by_user(self):
        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        with self.assertRaises(NotImplementedError):
            repo.find_by_user(u)

        repo = GenericRepository(Object)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        with self.assertRaises(NotImplementedError):
            repo.find_by_user(u)

    def test_find_by_id(self):
        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('83695382-5f71-11e8-9d7e-f40f2434c1ce')
        o1 = UserObject.objects.get(id=o_id)
        o2 = list(repo.find_by_id(pk=o_id, user=u))[0]
        self.assertEqual(o1, o2)

        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('87eca58a-5f71-11e8-b471-f40f2434c1ce')
        length = len(list(repo.find_by_id(pk=o_id, user=u)))
        self.assertEqual(1, length)

        repo = GenericRepository(Object)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('4343f01c-5f71-11e8-b73c-f40f2434c1ce')
        o2 = list(repo.find_by_id(pk=o_id, user=u))
        self.assertEqual(1, len(o2))

    def test_get_by_id(self):
        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('83695382-5f71-11e8-9d7e-f40f2434c1ce')
        o1 = UserObject.objects.get(id=o_id)
        o2 = repo.get_by_id(pk=o_id, user=u)
        self.assertEqual(o1, o2)

        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('87eca58a-5f71-11e8-b471-f40f2434c1ce')
        instance = repo.get_by_id(pk=o_id, user=u)
        self.assertEqual(o_id, instance.id)

        repo = GenericRepository(Object)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('4343f01c-5f71-11e8-b73c-f40f2434c1ce')
        instance = repo.get_by_id(pk=o_id, user=u)
        self.assertEqual(o_id, instance.id)

        repo = GenericRepository(Object)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('e488a5ba-5f78-11e8-b89d-f40f2434c1ce')
        with self.assertRaises(ObjectNotFoundError):
            repo.get_by_id(pk=o_id, user=u)

    def test_get_by_user_and_id(self):
        repo = OwnershipRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('83695382-5f71-11e8-9d7e-f40f2434c1ce')
        o1 = UserObject.objects.get(id=o_id)
        o2 = repo.get_by_id(pk=o_id, user=u)
        self.assertEqual(o1, o2)

        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('87eca58a-5f71-11e8-b471-f40f2434c1ce')
        instance = repo.get_by_id(pk=o_id, user=u)
        self.assertEqual(o_id, instance.id)

        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('fd88db5e-5f82-11e8-a7f9-f40f2434c1ce')
        with self.assertRaises(ObjectNotFoundError):
            repo.get_by_id(pk=o_id, user=u)

    def test_list_all(self):
        repo = GenericRepository(UserObject)
        l1 = len(list(UserObject.objects.all()))
        l2 = len(list(repo.list_all()))
        self.assertEqual(l1, l2)

    def test_persist(self):
        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        l1 = len(list(UserObject.objects.filter(owner=u)))
        instance = UserObject(name='A new user object', owner=u)
        repo.persist(instance)
        l2 = len(list(UserObject.objects.filter(owner=u)))
        self.assertEqual(l1, (l2 - 1))

    def test_delete_by_id(self):
        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        l1 = len(list(UserObject.objects.filter(owner=u)))
        o_id = str_to_uuid1('83695382-5f71-11e8-9d7e-f40f2434c1ce')
        repo.delete_by_id(pk=o_id, user=u)
        l2 = len(list(UserObject.objects.filter(owner=u)))
        self.assertEqual(l1, (l2 + 1))

        repo = GenericRepository(UserObject)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('87eca58a-5f71-11e8-b471-f40f2434c1ce')
        deleted = repo.delete_by_id(pk=o_id, user=u)
        self.assertEqual(True, deleted)

        repo = GenericRepository(Object)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        deleted = repo.delete_by_id(pk=o_id, user=u)
        self.assertEqual(True, deleted)

    def test_is_unique(self):
        repo = GenericRepository(Object)
        o_id = str_to_uuid1('4343f01c-5f71-11e8-b73c-f40f2434c1ce')
        obj = Object.objects.get(id=o_id)
        obj.name = 'Another Object'
        unique = repo.is_unique(obj, 'name')
        self.assertEqual(False, unique)

        repo = GenericRepository(Object)
        o_id = str_to_uuid1('4343f01c-5f71-11e8-b73c-f40f2434c1ce')
        obj = Object.objects.get(id=o_id)
        unique = repo.is_unique(obj, 'name')
        self.assertEqual(True, unique)

        repo = GenericRepository(Object)
        o_id = str_to_uuid1('4343f01c-5f71-11e8-b73c-f40f2434c1ce')
        obj = Object.objects.get(id=o_id)
        unique = repo.is_unique(obj, 'name')
        self.assertEqual(True, unique)

        repo = GenericRepository(Object)
        o_id = str_to_uuid1('4343f01c-5f71-11e8-b73c-f40f2434c1ce')
        obj = Object.objects.get(id=o_id)
        unique = repo.is_unique(obj, 'name')
        self.assertEqual(True, unique)

    def test_is_too_short(self):
        repo = GenericRepository(Object)
        pk = str_to_uuid1('4343f01c-5f71-11e8-b73c-f40f2434c1ce')
        instance = Object.objects.get(id=pk)
        too_short = repo.is_too_short(instance, 'name', 3)
        self.assertEqual(False, too_short)

        repo = GenericRepository(Object)
        pk = str_to_uuid1('4343f01c-5f71-11e8-b73c-f40f2434c1ce')
        instance = Object.objects.get(id=pk)
        too_short = repo.is_too_short(instance, 'name', 15)
        self.assertEqual(True, too_short)

    def test_contains_char_classes(self):
        repo = GenericRepository(Object)
        pk = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        classes = repo.contains_char_classes(instance, 'name', 1)
        self.assertEqual(True, classes)

        repo = GenericRepository(Object)
        pk = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        classes = repo.contains_char_classes(instance, 'name', 2)
        self.assertEqual(True, classes)

        repo = GenericRepository(Object)
        pk = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        classes = repo.contains_char_classes(instance, 'name', 3)
        self.assertEqual(False, classes)

        repo = GenericRepository(Object)
        pk = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        instance.name = 'aA#1'
        classes = repo.contains_char_classes(instance, 'name', 4)
        self.assertEqual(True, classes)

    def test_is_valid_email(self):
        repo = GenericRepository(User)
        pk = str_to_uuid1('53fbd124-1c69-11e8-941a-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        valid = repo.is_valid_email(instance, 'email')
        self.assertEqual(True, valid)

        repo = GenericRepository(User)
        pk = str_to_uuid1('53fbd124-1c69-11e8-941a-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        instance.email = 'not valid'
        valid = repo.is_valid_email(instance, 'email')
        self.assertEqual(False, valid)

        repo = GenericRepository(User)
        pk = str_to_uuid1('53fbd124-1c69-11e8-941a-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        instance.email = None
        valid = repo.is_valid_email(instance, 'email')
        self.assertEqual(True, valid)

        repo = GenericRepository(User)
        pk = str_to_uuid1('53fbd124-1c69-11e8-941a-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        instance.email = 'john.doeexample.com'
        valid = repo.is_valid_email(instance, 'email')
        self.assertEqual(False, valid)

        repo = GenericRepository(User)
        pk = str_to_uuid1('53fbd124-1c69-11e8-941a-f40f2434c1ce')
        instance = repo.get_by_id(pk)
        instance.email = 'john@example.com'
        valid = repo.is_valid_email(instance, 'email')
        self.assertEqual(True, valid)


class GenericValidatorTest(TransactionTestCase):
    fixtures = ['init.json']

    def test_is_value_unique(self):
        repo = GenericRepository(Object)
        o_id = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        o = Object.objects.get(id=o_id)

        validator = unique_field(repo, 'name')
        self.assertEqual(True, validator(o))

        repo = GenericRepository(Object)
        o = Object(name='Object')

        validator = unique_field(repo, 'name')
        with self.assertRaises(ValidationError):
            validator(o)

        repo = GenericRepository(Object)
        os = Object.objects.all()

        validator = unique_field(repo, 'name')
        self.assertEqual(True, validator(os))

    def test_validate_many(self):
        repo = GenericRepository(UserObject)
        o_id = str_to_uuid1('83695382-5f71-11e8-9d7e-f40f2434c1ce')
        o = UserObject.objects.get(id=o_id)

        validators = (unique_field(repo, 'name'),
                      unique_field(repo, 'owner'))
        checker = validate_many(*validators)
        self.assertEqual(True, checker(o))


class GenericServiceTest(TransactionTestCase):
    fixtures = ['init.json']

    def test_retrieve_single_service(self):
        repo = GenericRepository(Object)
        retrieve = generic_retrieve_single_service(repo)
        o_id = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        instance = retrieve(pk=o_id, requesting_user=None)
        self.assertEqual(o_id, instance.id)

    def test_retrieve_all(self):
        repo = GenericRepository(Object)
        retrieve = generic_retrieve_all_service(repo)
        length = len(retrieve())
        self.assertEqual(2, length)

    def test_retrieve_all_by_owner_service(self):
        repo = GenericRepository(Object)
        retrieve = generic_retrieve_all_by_owner_service(repo)
        with self.assertRaises(NotImplementedError):
            retrieve(requesting_user=None)

    def test_delete_service(self):
        repo = GenericRepository(Object)
        delete = generic_delete_service(repo)
        o_id = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        instance = delete(pk=o_id, requesting_user=u)
        self.assertEqual(o_id, instance.id)

        repo = GenericRepository(UserObject)
        delete = generic_delete_service(repo)
        o_id = str_to_uuid1('83695382-5f71-11e8-9d7e-f40f2434c1ce')
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        delete(pk=o_id, requesting_user=u)
        o_l = len(list(UserObject.objects.filter(id=o_id)))
        self.assertEqual(0, o_l)

        repo = GenericRepository(UserObject)
        delete = generic_delete_service(repo)
        o_id = str_to_uuid1('87eca58a-5f71-11e8-b471-f40f2434c1ce')
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        instance = delete(pk=o_id, requesting_user=u)
        self.assertEqual(o_id, instance.id)

    def test_update_service(self):
        repo = GenericRepository(Object)
        validator = (unique_field(repo, 'name'),)
        update = generic_update_service(repo, validate_many(*validator))
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('6ef912ae-5f71-11e8-bc5f-f40f2434c1ce')
        name = 'NewNameForOldObject'
        password = 'newSecure#1Pass'

        instance = update(pk=o_id, requesting_user=u, name=name, password=password)
        self.assertEqual(name, instance.name)
        self.assertEqual(True, check_password(password, instance.password))

        repo = GenericRepository(UserObject)
        validator = (unique_field(repo, 'name'),)
        update = generic_update_service(repo, validate_many(*validator))
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('83695382-5f71-11e8-9d7e-f40f2434c1ce')
        name = 'NewNameForOldObject'

        update(pk=o_id, requesting_user=u, name=name)
        o = UserObject.objects.get(id=o_id)
        self.assertEqual(o_id, o.id)
        self.assertEqual(name, o.name)

        repo = GenericRepository(UserObjectPw)
        validator = (unique_field(repo, 'name'),)
        update = generic_update_service(repo, validate_many(*validator))
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o_id = str_to_uuid1('603378ab-5f85-11e8-8ef9-f40f2434c1ce')
        name = 'NewNameForOldObject'
        password = 'NewSecurePassword#123'

        update(pk=o_id, requesting_user=u, name=name, password=password)
        o = UserObjectPw.objects.get(id=o_id)
        self.assertEqual(o_id, o.id)
        self.assertEqual(name, o.name)
        self.assertEqual(True, check_password(password, o.password))

    def test_create_service(self):
        repo = GenericRepository(Object)
        validator = (unique_field(repo, 'name'),)
        create = generic_create_service(repo,
                                        validate_many(*validator),
                                        generic_factory)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        password = 'New123Password'
        o1 = create(requesting_user=u, name='VeryNewObject', password=password)
        o2 = Object.objects.get(id=o1.id)
        self.assertEqual(o1, o2)
        self.assertEqual(True, check_password(password, o1.password))
        self.assertEqual(True, check_password(password, o2.password))

        repo = GenericRepository(UserObject)
        validator = (unique_field(repo, 'name'),)
        create = generic_create_service(repo,
                                        validate_many(*validator),
                                        generic_factory)
        user_id = str_to_uuid1('3f44d78a-1c69-11e8-a078-f40f2434c1ce')
        u = User.objects.get(id=user_id)
        o1 = create(requesting_user=u, name='VeryNewObject')
        o2 = UserObject.objects.get(id=o1.id)
        self.assertEqual(o1, o2)


class GenericViewTest(TransactionTestCase):
    fixtures = ['init.json']

    def test_create_view(self):
        user = User.objects.get(username='lisamorgan')
        client = APIClient()
        client.force_authenticate(user=user)

        l1 = len(list(UserObject.objects.all()))
        request = client.post('/objects.json', {'name': 'new name'}, format='json')
        l2 = len(list(UserObject.objects.all()))
        self.assertEqual(201, request.status_code)
        self.assertEqual(l1, (l2 - 1))

    def test_list_view(self):
        user = User.objects.get(username='lisamorgan')
        client = APIClient()
        client.force_authenticate(user=user)

        request = client.get('/objects.json', format='json')
        self.assertEqual(200, request.status_code)

    def test_retrieve_view(self):
        user = User.objects.get(username='lisamorgan')
        client = APIClient()
        client.force_authenticate(user=user)

        request = client.get('/objects/83695382-5f71-11e8-9d7e-f40f2434c1ce.json',
                             format='json')
        self.assertEqual(200, request.status_code)

    def test_destroy_view(self):
        user = User.objects.get(username='lisamorgan')
        client = APIClient()
        client.force_authenticate(user=user)

        l1 = len(list(UserObject.objects.all()))
        request = client.delete('/objects/83695382-5f71-11e8-9d7e-f40f2434c1ce.json',
                                format='json')
        l2 = len(list(UserObject.objects.all()))
        self.assertEqual(200, request.status_code)
        self.assertEqual(l1, (l2 + 1))

    def test_partial_update_view(self):
        user = User.objects.get(username='lisamorgan')
        client = APIClient()
        client.force_authenticate(user=user)

        request = client.patch('/objects/83695382-5f71-11e8-9d7e-f40f2434c1ce.json',
                               {'name': 'new name2'}, format='json')
        self.assertEqual(200, request.status_code)
