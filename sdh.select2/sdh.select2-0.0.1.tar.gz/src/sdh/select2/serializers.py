from rest_framework import serializers

from django.utils.text import Truncator


class Select2Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        text = getattr(obj, 'select2label', None) or getattr(obj, 'label', None)
        if text:
            return Truncator(text).chars(64)
        return text

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
