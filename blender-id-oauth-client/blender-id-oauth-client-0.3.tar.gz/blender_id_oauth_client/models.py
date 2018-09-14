from django.contrib.auth.models import User
from django.db import models


class OAuthToken(models.Model):
    """Store OAuth Tokens to perform OAuth requests.

    This is used after successful OAuth login to check if there is a user already
    associated with the returned oauth_user_id.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='oauth_tokens')
    provider = models.CharField(max_length=255)
    oauth_user_id = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    expires_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'OAuth Token'
        verbose_name_plural = 'OAuth Tokens'

    def __str__(self) -> str:
        return f'{self.provider} token of {self.user}'
