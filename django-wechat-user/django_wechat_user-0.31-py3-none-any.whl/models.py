from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(models.Model):
    """微信会员
    """

    openid = models.CharField(verbose_name=_("OpenID"), max_length=128, unique=True, db_index=True)
    last_logined_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"OpenId: {self.openid}"


class UserInfo(models.Model):

    # gender
    GENDER_UNKNOWN = 0
    GENDER_MALE = 1
    GENDER_FEMALE = 2

    # choices of gender
    GENDER_CHOICES = ((GENDER_UNKNOWN, _("Unknown")), (GENDER_MALE, _("Male")), (GENDER_FEMALE, _("Female")))

    owner = models.OneToOneField(
        "User", verbose_name=_("User"), related_name="info", related_query_name="info", on_delete=models.CASCADE
    )
    unionid = models.CharField(verbose_name=_("Union Id"), max_length=128, unique=True, blank=True, null=True)
    nickname = models.CharField(verbose_name=_("Nick name"), max_length=64, blank=True, null=True)
    avatar_url = models.URLField(verbose_name=_("Avatar URL"), max_length=255, blank=True, null=True)
    gender = models.SmallIntegerField(verbose_name=_("Gender"), choices=GENDER_CHOICES, default=GENDER_UNKNOWN)
    city = models.CharField(verbose_name=_("City"), max_length=32, blank=True, null=True)
    province = models.CharField(verbose_name=_("Province"), max_length=32, blank=True, null=True)
    country = models.CharField(verbose_name=_("Country"), max_length=32, blank=True, null=True)
    language = models.CharField(verbose_name=_("Language"), max_length=16, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return (
            "Owner: {} "
            "nickname: {} "
            "gender: {} "
            "country: {} "
            "province: {} "
            "country: {} "
        ).format(self.owner, self.nickname, self.gender, self.country, self.province, self.city)


class UserMobilePhone(models.Model):
    owner = models.OneToOneField(
        "User", verbose_name=_("User"), related_name="phone", related_query_name="phone", on_delete=models.CASCADE
    )
    number = models.CharField(verbose_name=("Phone number"), max_length=16)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
