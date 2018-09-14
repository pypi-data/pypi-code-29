# -*- coding:utf-8 -*-
# create_time: 2018/9/4 11:13
__author__ = 'brad'

from rest_framework import serializers
from . import models


class EndpointSerializer(serializers.HyperlinkedModelSerializer):
    counters = serializers.HyperlinkedRelatedField(many=True, view_name='counter-detail', read_only=True)
    tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail', read_only=True)
    snippet = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = models.Endpoint
        fields = "__all__"
        read_only_fields = ('endpoint', )
        extra_kwargs = {
            'ts': {
                'write_only': True
            },
            # 'url': {
            #     'view_name': '',
            #     'lookup_field': '',
            # }
        }
        depth = 2


class CounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Counter
        fields = "__all__"
        # exclude = ('url', )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"
