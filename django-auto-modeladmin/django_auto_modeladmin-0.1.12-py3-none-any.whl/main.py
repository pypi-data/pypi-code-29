from django.contrib import admin
from .utils import (
    filter_list,
    capitalize,
    find_fields,
    get_readonly_field_names,
    DATE_FIELD_NAMES,
    ID_FIELD_NAMES,
)
import nested_admin


def create_model_admin_inline(model):
    found_fields = find_fields(model)
    readonly_fields = get_readonly_field_names(found_fields["regular"])
    inlines = ()
    for related in found_fields["related"]:
        inlines += (create_model_admin_inline(related),)
    name = '{}AdminInline'.format(capitalize(model.__name__))
    bases = (nested_admin.NestedStackedInline,)
    attrs = {
        "model": model,
        "extra": 0,
        "readonly_fields": readonly_fields,
        "inlines": inlines
    }
    return type(name, bases, attrs)


def create_model_admin(model, config=None):
    """ Dynamically generate ModelAdmin classes for installed models.
        Display the form field based on the field name used.
        https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    """

    # Find the fields on the model.
    found_fields = find_fields(model)

    # get property fields that are provided
    property_field_names = list(config.get("property_fields", []))

    # fields to exclude_field_names from model admin
    exclude_field_names = list(config.get("exclude", [])) + found_fields["excluded"]

    # Fields that are displayed in list mode.
    list_display_field_names = list(config.get("list_display", []))

    # create a list of readonly fields to use that are on the model.
    readonly_field_names = get_readonly_field_names(
        found_fields["regular"],
        list(config.get("readonly_fields", [])) + property_field_names
    )

    # Create the fieldsets
    fieldsets = []

    # Create fieldset for id fields
    id_field_names = filter_list(
        found_fields["regular"],
        ID_FIELD_NAMES
    )
    if len(id_field_names):
        fieldsets.append(
            ("Ids", {
                "fields": id_field_names
            })
        )

    # Create fieldset for date fields
    date_field_names = filter_list(
        found_fields["regular"],
        DATE_FIELD_NAMES
    )
    if len(date_field_names):
        fieldsets.append(
            ("Dates", {
                "fields": date_field_names
            })
        )

    # Create the other fields
    other_field_names = [
        n for n in found_fields["regular"] + property_field_names
        if n not in date_field_names + id_field_names + exclude_field_names
    ]
    fieldsets.append(
        ("Other", {
            "fields": other_field_names
        })
    )

    # Create the model inlines
    inlines = ()
    for related_field in found_fields["related"]:
        inlines += (create_model_admin_inline(related_field),)

    # Create the ModelAdmin class
    name = '{}ModelAdmin'.format(capitalize(model.__name__))
    bases = (nested_admin.NestedModelAdmin,)
    attrs = {
        "readonly_fields": readonly_field_names,
        "list_display": list_display_field_names,
        "fieldsets": tuple(fieldsets),
        "inlines": inlines,
        "exclude": exclude_field_names,
    }
    return type(name, bases, attrs)


def autoregister(list_of_models):
    for model in list_of_models:
        if isinstance(model, tuple):
            model_instance = model[0]
            extra_list_display_field_names_found = model[1]
            model_admin = create_model_admin(
                model_instance, extra_list_display_field_names_found)
            admin.site.register(model_instance, model_admin)
        else:
            model_admin = create_model_admin(model)
            admin.site.register(model, model_admin)
