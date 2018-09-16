#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .db_constants import *

__all__ = ['User', 'Article', 'Reaction', 'AttachmentType', 'Attachment', 'Comment', 'Mention', 'Chat', 'ChatMember',
           'Message', 'UserMessage', ]


class User(models.Model):
    first_name = models.CharField(max_length=64, default=UserDefaults.first_name)
    last_name = models.CharField(max_length=64, default=UserDefaults.last_name)
    study_group = models.CharField(max_length=10, default=UserDefaults.study_group)
    birthday = models.DateField(auto_now_add=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='media/users/profile_pics', null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    lang = models.CharField(max_length=5, default=UserDefaults.lang)
    activated = models.BooleanField(default=UserDefaults.activated)
    is_staff = models.BooleanField(default=UserDefaults.is_staff, editable=False)

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

    @property
    def serialized(self) -> dict:
        return self._serialize()

    def _serialize(self) -> dict:
        from .serializers import UserSerializer
        return UserSerializer(self).data

    @property
    def serializer(self):
        from .serializers import UserSerializer
        return UserSerializer(self)


class Article(models.Model):
    body = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        db_table = '_Article'

    def __str__(self):
        return f'{self.user.email} - {self.timestamp}'

    @property
    def serialized(self) -> dict:
        return self._serialize()

    def _serialize(self) -> dict:
        return {
            'id': self.pk,
            'body': self.body,
            'timestamp': self.timestamp.strftime(Utils.DATETIME_FORMAT),
            'user': self.user.serialized,
        }

    @classmethod
    def deserialize(cls, data: dict, save: bool = False):
        article = Article()

        article.pk = data.get('id', ArticleDefaults.id)
        article.body = data.get('body', ArticleDefaults.body)
        article.timestamp = data.get('timestamp', ArticleDefaults.timestamp)

        user_dict: dict = data.get('user', ArticleDefaults.user)
        user_id: int = user_dict.get('id', UserDefaults.id)

        if user_id == 0:
            raise ValueError('Can not create article without user_id')
        elif User.objects.filter(pk=user_id).count() == 0:
            raise ValueError('User with passed id does not exist')

        article.user_id = user_id
        article.user = User.objects.get(pk=user_id)

        if save:
            article.save()

        return article


class Reaction(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = _('Reaction')
        verbose_name_plural = _('Reactions')
        unique_together = ('article', 'user')
        db_table = '_Reaction'

    def __str__(self):
        return f'{self.user.email} liked {str(self.article)} article'

    @property
    def serialized(self) -> dict:
        return self._serialize()

    def _serialize(self) -> dict:
        pass

    @classmethod
    def deserialize(cls, data: dict, save: bool = False):
        pass


class AttachmentType(models.Model):
    VIDEO = 0
    AUDIO = 1
    IMAGE = 2
    LINK = 3
    DOC = 4
    TYPE_CHOICES = (
        (VIDEO, 'Video'),
        (AUDIO, 'Audio'),
        (IMAGE, 'Image'),
        (LINK, 'Link'),
        (DOC, 'Document')
    )
    tag = models.IntegerField(choices=TYPE_CHOICES, default=DOC, unique=True)

    class Meta:
        verbose_name = _('Attachment Type')
        verbose_name_plural = _('Attachment Types')
        db_table = '_AttachmentType'

    def __str__(self):
        return f'{self.get_tag_display()}'


class Attachment(models.Model):
    attachment_type = models.ForeignKey(AttachmentType, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to=f'media/attachments/{attachment_type}/')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')
        db_table = '_Attachment'

    def __str__(self):
        return f'{self.file.name}'


class Comment(models.Model):
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


class Mention(models.Model):
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


class Chat(models.Model):

    class Meta:
        verbose_name = _('Chat')
        verbose_name_plural = _('Chats')
        db_table = '_Chat'

    def __str__(self):
        return f'{self.pk}'


class ChatMember(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Chat Member')
        verbose_name_plural = _('Chat Members')
        unique_together = ('chat', 'user')
        db_table = '_ChatMember'

    def __str__(self):
        return f'Chat: {self.chat.pk}; User: {self.user.email}'


class Message(models.Model):
    body = models.TextField(max_length=150)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        db_table = '_Message'

    def __str__(self):
        return f'Chat: {self.chat.pk}; Sender: {self.sender.pk}'


class UserMessage(models.Model):
    message = models.ForeignKey(Message, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('User Message')
        verbose_name_plural = _('User Messages')
        unique_together = ('message', 'user')
        db_table = '_UserMessage'

    def __str__(self):
        return f'User: {self.user.pk}; Message: {self.message.pk}'
