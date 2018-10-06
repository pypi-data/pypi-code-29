#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import *

__all__ = ('RoleSerializer', 'GroupSerializer', 'LanguageSerializer', 'UserSerializer', 'ArticleSerializer',
           'ReactionSerializer', 'AttachmentTypeSerializer', 'FileExtensionSerializer', 'AttachmentSerializer',
           'CommentSerializer', 'MentionSerializer', 'ChatMemberSerializer', 'MessageSerializer', 'ChatSerializer',
           'UserMessageSerializer')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = Group
        fields = ('id', 'code', 'role')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'code')


class UserSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    lang = LanguageSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'group', 'birthday', 'about', 'profile_pic', 'email', 'lang',
                  'activated')


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Article
        fields = ('id', 'body', 'timestamp', 'user')


class ReactionSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    user = UserSerializer()

    class Meta:
        model = Reaction
        fields = ('id', 'article', 'user')


class AttachmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachmentType
        fields = ('id', 'tag')


class FileExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileExtension
        fields = ('id', 'name')


class AttachmentSerializer(serializers.ModelSerializer):
    attachment_type = AttachmentTypeSerializer()
    article = ArticleSerializer()
    file_extension = FileExtensionSerializer()

    class Meta:
        model = Attachment
        fields = ('id', 'attachment_type', 'file', 'article', 'original_name', 'file_extension')


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'body', 'article', 'timestamp', 'user')


class MentionSerializer(serializers.ModelSerializer):
    comment = CommentSerializer()
    user = UserSerializer()

    class Meta:
        model = Mention
        fields = ('id', 'comment', 'had_seen', 'user')


class ChatMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ChatMember
        fields = ('id', 'chat', 'user')


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'body', 'chat', 'sender', 'timestamp')


class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(source='message_set', many=True)
    chat_members = ChatMemberSerializer(source='chatmember_set', many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'chat_members')


class UserMessageSerializer(serializers.ModelSerializer):
    messages = MessageSerializer()
    user = UserSerializer()

    class Meta:
        model = UserMessage
        fields = ('id', 'message', 'user')


_serializers: dict = {
    'Role': RoleSerializer,
    'Group': GroupSerializer,
    'Language': LanguageSerializer,
    'User': UserSerializer,
    'Article': ArticleSerializer,
    'Reaction': ReactionSerializer,
    'AttachmentType': AttachmentTypeSerializer,
    'FileExtension': FileExtensionSerializer,
    'Attachment': AttachmentSerializer,
    'Comment': CommentSerializer,
    'Mention': MentionSerializer,
    'ChatMember': ChatMemberSerializer,
    'Message': MessageSerializer,
    'Chat': ChatSerializer,
    'UserMessage': UserMessageSerializer
}


def get(class_name: str):
    if class_name in _serializers.keys():
        return _serializers.get(class_name)
    raise KeyError(f'Can not find {class_name} class')
