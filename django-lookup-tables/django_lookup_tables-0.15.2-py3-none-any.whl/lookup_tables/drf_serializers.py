from rest_framework import serializers

from .drf_fields import LookupSerializerField


class ModelWithLookupsSerializer(serializers.ModelSerializer):

    serializer_field_mapping = serializers.ModelSerializer.serializer_field_mapping.copy()
    serializer_field_mapping.update(
        {model: LookupSerializerField}
        for model in AbstractLookupTable.subclasses()
    )
