from django.core.exceptions import ImproperlyConfigured
from django.db.models.query import QuerySet

from generic.exceptions import ValidationError


def unique_field(repository, field):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that field is unique.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if not repository.is_unique(instance, field):
                raise ValidationError('This value has already been used.',
                                      field=field)
            return True

    return _checker


def unique_together_fields(repository, *fields):
    """
    :param repository: Repository that should be used to perform validation
    :param fields: Fields to be validated
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that the combination of fields is unique.
    Checks if a field is unique.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if len(repository.search_by(instance, *fields)) is not 0:
                raise ValidationError('These values have already been used.',
                                      field=fields)
            return True

    return _checker


def required_field(repository, field):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that field is present and not None.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.is_none(instance, field):
                raise ValidationError('Mandatory value was not provided.',
                                      field=field)
            return True

    return _checker


def max_length(repository, field, length):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :param length: Maximal length for field
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that the string in field comprises at most length characters.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.is_too_long(instance, field, length):
                raise ValidationError(("Maximal length of {0} chars "
                                       "exceeded.").format(length),
                                      field=field)
            return True

    return _checker


def min_length(repository, field, length):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :param length: Maximal length for field
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that the string in field comprises at least length characters.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.is_too_short(instance, field, length):
                raise ValidationError(("Minimal length of {0} characters "
                                       "not met.").format(length),
                                      field=field)

            return True

    return _checker


def read_only_field(repository, field):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that read only fields are not written to.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.contains_arg(instance, field):
                raise ValidationError('Attempt to write read only field.',
                                      field=field)
            return True

    return _checker


def min_char_classes(repository, field, char_classes):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :param char_classes: Number of different character classes need to be
    present; can be lower/upper case letters, digits or punctuation
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that the string in field comprises a sufficient amount of
    different character classes.
    """
    if char_classes < 0 or char_classes > 4:
        raise ImproperlyConfigured(("Number of character classes "
                                    "must be  in range 0-4."))

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if not repository.contains_char_classes(instance, field, char_classes):
                raise ValidationError(("Field must contain {0} of the "
                                       "following characters: upper case letters, "
                                       "lower case letters, digits and special "
                                       "characters.").format(char_classes),
                                      field='password')

            return True

    return _checker


def email_field(repository, field):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that an email address field is populated with a valid email
    address.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if not repository.is_valid_email(instance, field):
                raise ValidationError('This email address is invalid.', field='email')
            return True

    return _checker


def image_dim_validator(repository, field, width, height):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :param width: Maximum image width
    :param height: Maximum image height
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that an image is not too tall or wide.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.image_too_tall(instance, field, height):
                msg = "Image is too tall: Maximum height is {0}.".format(height)
                raise ValidationError(msg, field=field)
            if repository.image_too_wide(instance, field, width):
                msg = "Image is too wide: Maximum width is {0}.".format(width)
                raise ValidationError(msg, field=field)
            return True

    return _checker


def image_size_validator(repository, field, size):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :param size: Maximum image size in bytes
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that an image is not too large.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.image_too_large(instance, field, size):
                msg = "Image is too large: Maximum size is {}B.".format(size)
                raise ValidationError(msg, field=field)
            return True

    return _checker


def image_square_validator(repository, field):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :return: ValidationError if the validation failed

    Ensures that image is quadratic.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if not repository.is_square(instance, field):
                msg = 'Image must be quadratic.'
                raise ValidationError(msg, field=field)
            return True

    return _checker


def validate_many(*validators):
    """
    :param validators: List of validators to be applied

    Allows to apply multiple validators on one instance.
    """

    def _checker(instance):
        return all(validator(instance) for validator in validators)

    return _checker


def file_size_validator(repository, field, size):
    """
    :param repository: Repository that should be used to perform validation
    :param field: Field to be validated
    :param size: Maximum image size in bytes
    :return: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that a file is not too large.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.file_too_large(instance, field, size):
                msg = "File is too large: Maximum size is {}B.".format(size)
                raise ValidationError(msg, field=field)
            return True

    return _checker
