from django.conf import settings
import jwt


def jwt_get_username_from_payload_handler(payload):
    return payload.get('uuid')


def jwt_decode_handler(token):
    options = {
        'verify_exp': settings.AUTH_JWT_VERIFY_EXPIRATION,
    }

    return jwt.decode(
        token,
        settings.AUTH_JWT_SECRET_KEY,
        settings.AUTH_JWT_VERIFY,
        options=options,
        leeway=settings.AUTH_JWT_LEEWAY,
        audience=settings.AUTH_JWT_AUDIENCE,
        issuer=settings.AUTH_JWT_ISSUER,
        algorithms=[settings.AUTH_JWT_ALGORITHM]
    )
