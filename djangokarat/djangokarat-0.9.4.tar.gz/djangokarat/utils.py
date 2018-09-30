def has_karat_fields(instance):
    if not instance._meta.karat_table and not instance._meta.karat_fields:
        return False
    return True


def convert__all__to_fields(instance):
    # Checks meta karat_fields for __all__ to add to fields
    if (instance._meta.karat_table and not instance._meta.karat_fields) or instance._meta.karat_fields == '__all__':
        instance._meta.karat_fields = [f.name for f in instance._meta.get_fields()]


def get_karat_id_field(instance):
    pass


def filter_relational_fields(list):
    return [field for field in list if '__' in field]
