from django.contrib.auth.hashers import make_password
from rest_framework.utils import model_meta

from generic.repositories import GenericRepository


def generic_retrieve_single_service(repository):
    """
    :param repository: Repository that will be called
    :return: Instance matching pk

    Returns an instance by pk.
    """

    def _retrieve(pk, requesting_user):
        instance = repository.get_by_id(pk, requesting_user)
        return instance

    return _retrieve


def generic_retrieve_all_service(repository):
    """
    :param repository: Repository that will be called
    :return: Queryset with all stored instances

    Returns all stored instances.
    """

    def _retrieve(requesting_user=None):
        instances = repository.list_all()
        return instances

    return _retrieve


def generic_retrieve_all_by_owner_service(repository):
    """
    :param repository: Repository that will be called
    :return: Queryset with all owned instances

    Returns all stored instances owned by user.
    """

    def _retrieve(requesting_user):
        instances = repository.find_by_user(requesting_user)
        return instances

    return _retrieve


def generic_delete_service(repository):
    """
    :param repository: Repository that will be called
    :return: Instance that was deleted

    Deletes an instance by pk.
    """

    def _delete(pk, requesting_user):
        instance = repository.get_by_id(pk, requesting_user)
        repository.delete_by_id(pk, requesting_user)
        return instance

    return _delete


def generic_update_service(repository, validator):
    """
    :param repository: Repository that will be called
    :param validator: Instance validator
    :return: Updated and saved instance

    Updates an existing instance.
    """

    def _update(pk, requesting_user, **kwargs):

        # Get instance and meta info
        info = model_meta.get_field_info(repository.model_class)
        instance = repository.get_by_id(pk, requesting_user)

        # One-to-many relations
        for field_name, relation_info in info.relations.items():
            if (not relation_info.to_many
                    and field_name in kwargs.keys()
                    and kwargs[field_name] is not None):
                model = relation_info.related_model

                pk = kwargs[field_name]
                repo = GenericRepository(model)
                related_instance = repo.get_by_id(pk)

                setattr(instance, field_name, related_instance)

        # Set regular fields and validate
        for field_name, field_info in info.fields.items():
            if field_name in kwargs.keys():
                setattr(instance, field_name, kwargs[field_name])

        validator(instance)

        # Set hashed password
        if hasattr(repository.model_class, 'password') and 'password' in kwargs:
            instance.password = make_password(kwargs['password'])

        # Save and return
        repository.persist(instance)
        return instance

    return _update


def generic_create_service(repository, validator, factory):
    """
    :param repository: Repository that will be called
    :param validator: Instance validator
    :param factory: Factory that creates the instance
    :return: Created and saved instance

    Returns and persists a new instance.
    """

    def _create(requesting_user, **kwargs):

        # Get owner and meta info
        info = model_meta.get_field_info(repository.model_class)
        if hasattr(repository.model_class, 'owner'):
            kwargs['owner'] = requesting_user.id

        # One-to-many relations
        for field_name, relation_info in info.relations.items():
            if (not relation_info.to_many
                    and field_name in kwargs.keys()
                    and kwargs[field_name] is not None):
                model = relation_info.related_model

                pk = kwargs[field_name]
                repo = GenericRepository(model)
                related_instance = repo.get_by_id(pk)

                kwargs[field_name] = related_instance

        # Create instance and validate
        instance = factory(repository.model_class, **kwargs)
        validator(instance)

        # Set hashed password
        if hasattr(repository.model_class, 'password') and 'password' in kwargs:
            instance.password = make_password(kwargs['password'])

        # Save and return
        repository.persist(instance)
        return instance

    return _create


def store_image_service(repository, validator, field):
    """
    :param repository: Repository that will be called
    :param validator: Instance validator
    :param field: Name of ImageField
    :return: instance with image

    Adds image to instance. Also stores image on disk.
    """

    def _store(instance, image):
        instance = repository.store_image(instance, image, field)
        validator(instance)
        instance.save()
        return instance

    return _store


def remove_image_service(repository, field):
    """
    :param repository: Repository that will be called
    :param field: Name of ImageField
    :return: User instance without image

    Removes image from instance. Also deletes image from disk.
    """

    def _remove(pk, requesting_user):
        instance = repository.get_by_id(pk, requesting_user)
        image = getattr(instance, field)
        image.delete(save=True)
        return instance

    return _remove


def store_file_service(repository, validator, field):
    """
    :param repository: Repository that will be called
    :param validator: Instance validator
    :param field: Name of FileField
    :return: instance with file

    Adds file to instance. Also stores file on disk.
    """

    def _store(instance, file):
        instance = repository.store_file(instance, file, field)
        validator(instance)
        instance.save()
        return instance

    return _store


def remove_file_service(repository, field):
    """
    :param repository: Repository that will be called
    :param field: Name of FileField
    :return: User instance without file

    Removes file from instance. Also deletes file from disk.
    """

    def _remove(pk, requesting_user):
        instance = repository.get_by_id(pk, requesting_user)
        file = getattr(instance, field)
        file.delete(save=True)
        return instance

    return _remove
