from django.conf import settings
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

BLOG_PAGINATION = (getattr(settings, 'BLOG_PAGINATION', 20))