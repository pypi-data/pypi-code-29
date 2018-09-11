import re

from django.core.exceptions import ObjectDoesNotExist

from generic.exceptions import ObjectNotFoundError
from generic.helpers import contains_char_classes


class ValidatorMixin:
    """
    Provides validators for generic repositories.
    """

    def is_unique(self, instance, field):
        """
        :param instance: Instance that should be validated
        :param field: Field that should be checked for uniqueness
        :return: True if the value stored in field is unique; False otherwise

        Checks the uniqueness of the value stored in field.
        Cannot be used as an argument validator.
        """
        try:
            value = getattr(instance, field)
        except KeyError:
            return True

        if value is None:
            return True

        kwargs = {field: str(value)}
        pk = getattr(instance, 'id')
        conflict = self.model_class.objects.exclude(id=pk).filter(**kwargs).count()

        if conflict is 0:
            return True

        return False

    def search_by(self, instance, *fields):
        """
        :param instance: Instance that should be validated
        :param fields: Fields that should be used as filter criteria
        :return: Queryset matching the filter criteria

        Returns queryset matching the filter criteria, excluding the passed
        instance.
        Cannot be used as an argument validator.
        """
        search_filter = {}

        def _get_value(field):
            try:
                value = getattr(instance, field)
            except KeyError:
                return

            search_filter[field] = value

        [_get_value(f) for f in fields]
        pk = getattr(instance, 'id')
        instances = self.model_class.objects.exclude(id=pk).filter(**search_filter)
        return instances

    @staticmethod
    def is_none(instance, field):
        """
        :param instance: Instance that should be validated
        :param field: field: Field that should be checked for None
        :return: True if the value stored in field is None; False otherwise

        Checks if the value stored in field is None.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return True

        if value is None:
            return True

        return False

    @staticmethod
    def is_too_long(instance, field, length):
        """
        :param instance: Instance that should be validated
        :param field: field: Field that should be checked for length
        :return: True if the value stored in field if longer than length;
        False otherwise

        Checks if the value stored in field is longer then max_length.
        Only applicable to CharFields.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return False

        if value is None:
            return False

        if len(value) > length:
            return True

        return False

    @staticmethod
    def is_too_short(instance, field, length):
        """
        :param instance: Instance that should be validated
        :param field: field: Field that should be checked for length
        :return: True if the value stored in field if shorter than length;
        False otherwise

        Checks if the value stored in field is shorter then length.
        Only applicable to CharFields.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return False

        if value is None:
            return False

        if len(value) < length:
            return True

        return False

    @staticmethod
    def contains_arg(instance, field):
        """
        :param instance: Instance that should be validated
        :param field: field: Field that should be checked for presence
        :return: True if the argument is present; False otherwise

        Checks if field is present in the args dictionary or instance.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                instance[field]
            else:
                getattr(instance, field)

        except KeyError:
            return False

        return True

    @staticmethod
    def contains_char_classes(instance, field, char_classes):
        """
        :param instance: Instance that should be validated
        :param field: Field that should be checked for character classes
        :param char_classes: Number of character classes that must be present
        :return: True if the value stored in field contains sufficient
        character classes, False otherwise

        Checks if the value stored in field contains the demanded number of
        different character classes.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return True

        if value is None:
            return True

        if contains_char_classes(value, char_classes):
            return True

        return False

    @staticmethod
    def is_valid_email(instance, field):
        """
        :param instance: Instance that should be validated
        :param field: Field that should be checked for a valid email address
        :return: True if the value stored in field is a valid email address;
        False otherwise

        Checks if the value stored in field is a valid email address.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return True

        if value is None:
            return True

        reg_ex = r"[^@]+@[^@]+\.[^@]+"
        if re.match(reg_ex, value):
            return True

        return False


class GenericRepository(ValidatorMixin):
    """
    Provides a generic database abstraction layer for all model classes.
    """

    def __init__(self, model_class):
        """
        :param model_class: Class of the model that this repository should
        work on.

        Constructor that initializes the repository with a specific
        model class.
        """
        self.model_class = model_class

    def find_by_user(self, user=None):
        """
        :raises: NotImplementedError
        """
        raise NotImplementedError("""GenericRepository does not provide
                                  function find_by_user.""")

    def find_by_id(self, pk, user=None):
        """
        :param pk: Primary key of the instance that should be returned
        :return: Queryset representing the instance with id=pk

        Provides generic get by id function. Returns queryset representing
        exactly one instance or an empty queryset.
        """
        return self.model_class.objects.filter(id=pk)

    def get_by_id(self, pk, user=None):
        """
        :param pk: Primary key of the instance that should be returned
        :return: Requested instance with id=pk
        :raises: ObjectNotFoundError if the requested object was not found

        Provides generic get by id function. Returns exactly one instance or
        raises error.
        """
        try:
            return self.model_class.objects.get(id=pk)
        except ObjectDoesNotExist:
            raise ObjectNotFoundError('Object not found.',
                                      modelclass=self.model_class)

    def list_all(self, user=None):
        """
        :return: Queryset of all instances

        Provides generic list all function.
        """
        return self.model_class.objects.all()

    def delete_by_id(self, pk, user=None):
        """
        :param pk: Primary key of the instance that should be deleted
        :return: True if the instance was deleted
        :raises: ObjectNotFoundError if the requested object was not found

        Provides generic delete function.
        """
        try:
            self.model_class.objects.get(id=pk).delete()
            return True
        except ObjectDoesNotExist:
            raise ObjectNotFoundError('Object not found.',
                                      modelclass=self.model_class)

    @staticmethod
    def persist(instance):
        """
        :param instance: Instance that should be persisted
        :return: The persisted instance

        Provides generic persist function.
        """
        return instance.save()


class OwnershipRepository(ValidatorMixin):
    """
    Provides a generic database abstraction layer for all model classes
    that have an owner field, writing and reading of these model classes is
    limited to the owner. At time of creation the ownership information is
    automatically inserted.
    """

    def __init__(self, model_class):
        """
        :param model_class: Class of the model that this repository should
        work on.

        Constructor that initializes the repository with a specific
        model class.
        """
        self.model_class = model_class

    def find_by_user(self, user):
        """
        :param user: Requesting user
        :return: Queryset representing all instances owned by user

        Provides generic find by user function.
        """
        if hasattr(self.model_class, 'owner'):
            return self.model_class.objects.filter(owner=user)

        return self.model_class.objects.filter(id=user.id)

    def find_by_id(self, pk, user):
        """
        :param pk: Primary key of the instance that should be returned
        :param user: Requesting user
        :return: Queryset representing the instance owned by user with id=pk

        Provides generic get by id function. Only matches instances that are
        owned by the user. If there is no owner field, id is used for
        determining ownership instead. Returns queryset representing exactly
        one instance or an empty queryset.
        """
        if hasattr(self.model_class, 'owner'):
            return self.model_class.objects.filter(owner=user).filter(id=pk)

        return self.model_class.objects.filter(id=user.id).filter(id=pk)

    def get_by_id(self, pk, user):
        """
        :param pk: Primary key of the instance that should be returned
        :param user: Requesting user
        :return: Requested instance owned by user with id=pk
        :raises: ObjectNotFoundError if the requested object was either not
        found or not owned by user

        Provides generic get by id function. Only matches instances that are
        owned by the user. If there is no owner field, id is used for
        determining ownership instead. Returns exactly one instance or
        raises error.
        """
        if hasattr(self.model_class, 'owner'):
            try:
                return self.model_class.objects.filter(owner=user).get(id=pk)
            except ObjectDoesNotExist:
                raise ObjectNotFoundError('Object not found.',
                                          modelclass=self.model_class)

        try:
            return self.model_class.objects.filter(id=user.id).get(id=pk)
        except (ObjectDoesNotExist, AttributeError):
            raise ObjectNotFoundError('Object not found.',
                                      modelclass=self.model_class)

    def list_all(self, user):
        """
        :param user: Requesting user
        :return: Queryset of instances owned by the user

        Provides generic list all owned by user function. If there is no owner
        field, id is used for determining ownership instead.
        """
        if hasattr(self.model_class, 'owner'):
            return self.model_class.objects.filter(owner=user)

        return self.model_class.objects.filter(id=user.id)

    def delete_by_id(self, pk, user):
        """
        :param pk: Primary key of the instance that should be deleted
        :param user: Requesting user
        :return: Instance that was deleted
        :raises: ObjectNotFoundError if the requested object was either not
        found or not owned by user

        Provides generic delete function. Only matches instances that are
        owned by the user. If there is no owner field, id is used for
        determining ownership instead.
        """
        if hasattr(self.model_class, 'owner'):
            try:
                return self.model_class.objects.filter(owner=user).get(id=pk).delete()
            except ObjectDoesNotExist:
                raise ObjectNotFoundError('Object not found.',
                                          modelclass=self.model_class)

        try:
            return self.model_class.objects.filter(id=user.id).get(id=pk).delete()
        except (ObjectDoesNotExist, AttributeError):
            raise ObjectNotFoundError('Object not found.',
                                      modelclass=self.model_class)

    @staticmethod
    def persist(instance):
        """
        :param instance: Instance that should be persisted
        :return: The persisted instance

        Provides generic persist function.
        """
        return instance.save()


class ImageRepository:
    """
    Provides a generic abstraction layer for handling images.
    """

    def __init__(self, model_class=None):
        """
        :param model_class: Class of the model that this repository should
        work on.

        Constructor that initializes the repository with a specific
        model class.
        """
        self.model_class = model_class

    @staticmethod
    def store_image(instance, image, field):
        """
        :param instance: Instance with ImageField
        :param image: Image that should be added to instance
        :param field: Name of the ImageField
        :return: Instance with image set to field; not save yet

        Add image to instance but does not save the instance or the image.
        instance.save() must be called to persist changes.
        """
        setattr(instance, field, image)
        return instance

    @staticmethod
    def image_too_tall(instance, field, height):
        """
        :param instance: Instance that should be validated
        :param field: Name of the ImageField
        :param height: Maximum height
        :return: True if the image is too tall; False otherwise

        Checks if an image is too tall, non-existing images are not
        considered too tall.
        """
        try:
            image = getattr(instance, field)
        except KeyError:
            return False

        if image.height > height:
            return True

        return False

    @staticmethod
    def image_too_wide(instance, field, width):
        """
        :param instance: Instance that should be validated
        :param field: Name of the ImageField
        :param width: Maximum width
        :return: True if the image is too wide; False otherwise

        Checks if an image is too wide, non-existing images are not
        considered too wide.
        """
        try:
            image = getattr(instance, field)
        except KeyError:
            return False

        if image.width > width:
            return True

        return False

    @staticmethod
    def image_too_large(instance, field, size):
        """
        :param instance: Instance that should be validated
        :param field: Name of the ImageField
        :param size: Maximum size in bytes
        :return: True if the image is larger that size; False otherwise

        Checks if an image is too large in terms of bytes, non-existing
        images are not considered too large.
        """
        try:
            image = getattr(instance, field)
        except KeyError:
            return False

        if image.size > size:
            return True

        return False

    @staticmethod
    def is_square(instance, field):
        """
        :param instance: Instance that should be validated
        :param field: Name of the ImageField
        :return: True is the image is quadratic; False otherwise

        Checks if an image is quadratic, non-existing images are considered
        quadratic.
        """
        try:
            image = getattr(instance, field)
        except KeyError:
            return True

        if image.width == image.height:
            return True

        return False


class FileRepository:
    """
    Provides a generic abstraction layer for handling files.
    """

    def __init__(self, model_class=None):
        """
        :param model_class: Class of the model that this repository should
        work on.

        Constructor that initializes the repository with a specific
        model class.
        """
        self.model_class = model_class

    @staticmethod
    def store_file(instance, file, field):
        """
        :param instance: Instance with FileField
        :param file: File that should be added to instance
        :param field: Name of the ImageField
        :return: Instance with file set to field; not save yet

        Add file to instance but does not save the instance or the file.
        instance.save() must be called to persist changes.
        """
        setattr(instance, field, file)
        return instance

    @staticmethod
    def file_too_large(instance, field, size):
        """
        :param instance: Instance that should be validated
        :param field: Name of the FileField
        :param size: Maximum size in bytes
        :return: True if the file is larger that size; False otherwise

        Checks if a file is too large in terms of bytes, non-existing
        files are not considered too large.
        """
        try:
            image = getattr(instance, field)
        except KeyError:
            return False

        if image.size > size:
            return True

        return False
