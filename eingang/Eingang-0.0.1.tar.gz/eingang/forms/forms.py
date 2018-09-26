from flask import flash
from flask_security.confirmable import requires_confirmation
from flask_security.forms import (
    ChangePasswordForm,
    email_required, email_validator,
    EqualTo, ForgotPasswordForm, LoginForm,
    password_length, password_required, ResetPasswordForm,
    Required, valid_user_email,
)
from flask_security.utils import (
    _datastore, hash_password, get_message, verify_and_update_password
)
from wtforms import Field, PasswordField, StringField, SubmitField, validators


class ExtendedLoginForm(LoginForm):
    email = StringField(
        label='',
        validators=[Required(
            message='EMAIL_NOT_PROVIDED'), validators.Email()],
        render_kw={
            'placeholder': 'Email address',
            'class': 'form-control',
        },
    )
    password = PasswordField(
        label='',
        validators=[password_required],
        render_kw={
            'placeholder': 'Password',
            'class': 'form-control',
        },
    )
    submit = SubmitField(
        label='Login',
        render_kw={
            'class': 'btn btn-primary',
        }
    )

    def validate(self):
        if not super(LoginForm, self).validate():
            return False
        self.user = _datastore.get_user(self.email.data)
        if self.user is None:
            return False
        if not self.user.password:
            self.password.errors.append(get_message('PASSWORD_NOT_SET')[0])
            return False
        if not verify_and_update_password(self.password.data, self.user):
            return False
        if requires_confirmation(self.user):
            self.email.errors.append(get_message('CONFIRMATION_REQUIRED')[0])
            return False
        if not self.user.is_active:
            self.email.errors.append(get_message('DISABLED_ACCOUNT')[0])
            return False
        return True


class ExtendedForgotPasswordForm(ForgotPasswordForm):
    email = StringField(
        label='',
        validators=[email_required, email_validator, valid_user_email],
        render_kw={
            'placeholder': 'Email address',
            'class': 'form-control',
        },
    )
    submit = SubmitField(
        label='Recover password',
        render_kw={
            'class': 'btn btn-primary',
        }
    )


class ExtendedResetPasswordForm(ResetPasswordForm):
    password = PasswordField(
        label='',
        validators=[password_required, password_length],
        render_kw={
            'placeholder': 'Password',
            'class': 'form-control',
        },
    )
    password_confirm = PasswordField(
        label='',
        validators=[
            EqualTo('password', message='RETYPE_PASSWORD_MISMATCH'),
            password_required,
        ],
        render_kw={
            'placeholder': 'Retype password',
            'class': 'form-control',
        },
    )
    submit = SubmitField(
        label='Reset password',
        render_kw={
            'class': 'btn btn-primary',
        }
    )


class ExtendedChangePasswordForm(ChangePasswordForm):
    password = PasswordField(
        label='',
        validators=[password_required],
        render_kw={
            'placeholder': 'Current password',
            'class': 'form-control',
        },
    )
    new_password = PasswordField(
        label='',
        validators=[password_required, password_length],
        render_kw={
            'placeholder': 'New password',
            'class': 'form-control',
        },
    )
    new_password_confirm = PasswordField(
        label='',
        validators=[
            EqualTo('new_password', message='RETYPE_PASSWORD_MISMATCH'),
            password_required,
        ],
        render_kw={
            'placeholder': 'Retype new password',
            'class': 'form-control',
        },
    )
    submit = SubmitField(
        label='Change password',
        render_kw={
            'class': 'btn btn-primary',
        }
    )
