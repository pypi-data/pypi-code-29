from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

JWT_VERIFY_EXPIRATION = False
JWT_VERIFY = True
JWT_LEEWAY = 0
JWT_AUDIENCE = None
JWT_ISSUER = None
JWT_ALGORITHM = 'HS256'

JWT_AUTH = {
    'JWT_DECODE_HANDLER': 'auth_uuid.helper_jwt.jwt_decode_handler',
    'JWT_PAYLOAD_GET_USERNAME_HANDLER': 'auth_uuid.helper_jwt..jwt_get_username_from_payload_handler'
}

JWT_SECRET_KEY = getattr(settings, 'JWT_SECRET_KEY', '')
URL_VALIDATE_USER_UUID = getattr(settings, 'URL_VALIDATE_USER_UUID', '')

LOGGER_NAME = 'auth_uuid'

if not JWT_SECRET_KEY or not URL_VALIDATE_USER_UUID:
    raise ImproperlyConfigured("JWT_SECRET_KEY and URL_VALIDATE_USER_UUID are required")
