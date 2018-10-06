from rest_framework import serializers
from .models import User, UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.get(openid=validated_data["openid"])
        info = UserInfo(
            owner=user,
            unionid=validated_data["unionid"],
            nickname=validated_data["nickname"],
            avatar_url=validated_data["headimgurl"],
            gender=validated_data["sex"],
            city=validated_data["city"],
            province=validated_data["province"],
            country=validated_data["country"]
        )
        info.save()
        return info


class UserSerializer(serializers.ModelSerializer):
    info = UserInfoSerializer(required=False)

    class Meta:
        model = User
        fields = "__all__"
        depth = 1
        extra_kwargs = {'token': {'write_only': True}}
    