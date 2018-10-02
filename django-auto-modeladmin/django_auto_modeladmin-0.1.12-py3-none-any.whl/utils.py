from django.db.models.fields.reverse_related import ManyToOneRel

ID_FIELD_NAMES = ["id", "uuid"]
DATE_FIELD_NAMES = ["created_on", "modified_on"]
READONLY_FIELD_NAMES = ID_FIELD_NAMES + DATE_FIELD_NAMES + ["slug"]

def get_readonly_field_names(field_names, additional_field_names=[]):
    return filter_list(
        field_names,
        list(set(READONLY_FIELD_NAMES + additional_field_names))
    )

def filter_list(list_to_check, list_to_include):
    """ Return a list with only items that matched an item in list_to_include.
    """
    filtered_list = []
    for checked in list_to_check:
        for included in list_to_include:
            if checked == included:
                filtered_list.append(checked)
    return filtered_list

def capitalize(string):
    """ helper function to create capitalized copy of string. """
    return string[:1].upper() + string[1:]

def find_fields(model):
    related = []
    regular = []
    excluded = []
    # orgnanize the fields, field_names based on teh field type.
    for field in model._meta.get_fields():
        # Reverse relationships
        if field.auto_created and not field.concrete:
            # Only create inlines for reverse-relationship FK fields attached to this model instance. (reverse FK relationships only)
            if isinstance(field, ManyToOneRel):
                related.append(field.related_model)
        else:
            try:
                if field.m2m_reverse_name.args[0].through is None:
                    related.append(field.name)
                else:
                    excluded.append(field.name)
            except AttributeError:
                regular.append(field.name)
    return {
        "related": related,
        "regular": regular,
        "excluded": excluded,
    }
