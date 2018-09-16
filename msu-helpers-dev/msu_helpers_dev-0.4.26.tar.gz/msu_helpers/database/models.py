#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import SerializableModel
from .db_constants import *

__all__ = ('StudyGroup', 'Language', 'User', 'Article', 'Reaction', 'AttachmentType', 'FileExtension', 'Attachment',
           'Comment', 'Mention', 'Chat', 'ChatMember', 'Message', 'UserMessage')


class StudyGroup(SerializableModel):
    code = models.CharField(max_length=10, default=UserDefaults.study_group, unique=True)

    class Meta:
        verbose_name = _('StudyGroup')
        verbose_name_plural = _('StudyGroups')
        db_table = '_StudyGroup'

    def __str__(self):
        return f'{self.code}'


class Language(SerializableModel):
    RU_RU = Language.RU_RU
    EN_US = Language.RU_RU
    LANG_CHOICES = (
        (RU_RU, 'Русский'),
        (EN_US, 'English')
    )
    code = models.CharField(choices=LANG_CHOICES, max_length=5, default=RU_RU, unique=True)

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
        db_table = '_Language'

    def __str__(self):
        return f'{self.code}'


class User(SerializableModel):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, null=True, blank=True)
    birthday = models.DateField(auto_now_add=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='media/users/profile_pics', null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING, null=True, blank=True)
    activated = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, editable=False)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = '_User'

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Article(SerializableModel):
    body = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        db_table = '_Article'

    def __str__(self):
        return f'{self.user.email} - {self.timestamp}'


class Reaction(SerializableModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = _('Reaction')
        verbose_name_plural = _('Reactions')
        unique_together = ('article', 'user')
        db_table = '_Reaction'

    def __str__(self):
        return f'{self.user.email} liked {str(self.article)} article'


class AttachmentType(SerializableModel):
    tag = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = _('Attachment Type')
        verbose_name_plural = _('Attachment Types')
        db_table = '_AttachmentType'

    def __str__(self):
        return f'{self.tag}'


class FileExtension(SerializableModel):
    name = models.CharField(max_length=10, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = _('FileExtension')
        verbose_name_plural = _('FileExtensions')
        db_table = '_FileExtension'

    def __str__(self):
        return f'{self.name}'


class Attachment(SerializableModel):
    attachment_type = models.ForeignKey(AttachmentType, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to=f'media/attachments/{attachment_type}/')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    original_name = models.CharField(max_length=100)
    file_extension = models.ForeignKey(FileExtension, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')
        db_table = '_Attachment'

    def __str__(self):
        return f'{self.file.name}'


class Comment(SerializableModel):
    body = models.TextField(max_length=150)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        db_table = '_Comment'

    def __str__(self):
        return f"{self.user.email} commented under {self.article.user.email}'s article at {self.timestamp}"


class Mention(SerializableModel):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    had_seen = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Mention')
        verbose_name_plural = _('Mentions')
        unique_together = ('comment', 'user')
        db_table = '_Mention'

    def __str__(self):
        return f'{self.comment.user.email} mentioned {self.user.email} in his comment ({self.had_seen})'


class Chat(SerializableModel):
    class Meta:
        verbose_name = _('Chat')
        verbose_name_plural = _('Chats')
        db_table = '_Chat'

    def __str__(self):
        return f'{self.pk}'


class ChatMember(SerializableModel):
    chat = models.ForeignKey(Chat, related_name='chat_members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Chat Member')
        verbose_name_plural = _('Chat Members')
        unique_together = ('chat', 'user')
        db_table = '_ChatMember'

    def __str__(self):
        return f'Chat: {self.chat.pk}; User: {self.user.email}'


class Message(SerializableModel):
    body = models.TextField(max_length=150)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        db_table = '_Message'

    def __str__(self):
        return f'Chat: {self.chat.pk}; Sender: {self.sender.pk}'


class UserMessage(SerializableModel):
    message = models.ForeignKey(Message, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('User Message')
        verbose_name_plural = _('User Messages')
        unique_together = ('message', 'user')
        db_table = '_UserMessage'

    def __str__(self):
        return f'User: {self.user.pk}; Message: {self.message.pk}'
