from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models


class PFPContentType(models.Model):
    """ContentTypes to create PerFieldPermissions for."""
    content_type = models.OneToOneField(ContentType, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content_type)


class PFPRoleType(models.Model):
    """Role types (e.g. User, Group) to allow users to filter available roles with."""
    role_ctype = models.OneToOneField(ContentType, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.role_ctype)


class PFPFilterType(models.Model):
    """ContentTypes to make available when managing permissions."""
    filter_ctype = models.OneToOneField(ContentType, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.role_ctype)


class PerFieldPermission(Permission):
    """Extends Permission to enable field level permissions."""
    field_name = models.CharField(max_length=100, blank=False, null=False)
    model_permission = models.ForeignKey(
            Permission,
            null=False,
            blank=False,
            on_delete=models.CASCADE,
            related_name='field_permissions',
            )

    class Meta:
        permissions = (('manage_permissions', 'Can manage permissions'),)

    def clean(self):
        """Ensure a PFP has the same ContentType as its parent Permission."""
        if self.content_type_id != self.model_permission.content_type_id:
            raise ValidationError('PerFieldPermission model_permission must be of the same '
                                  'ContentType as self.')
        super().clean()

    def validate_unique(self, exclude=None):
        """
        Ensure only one PFP exists for a given Permission/field combination.
        """
        super().validate_unique(exclude)
        try:
            perm = PerFieldPermission.objects.get(
                    codename=self.codename,
                    model_permission=self.model_permission,
                    )
        except ObjectDoesNotExist:
            return

        if ((hasattr(self, 'pk') and self.pk != perm.pk)
                or not hasattr(self, 'pk')):
            raise ValidationError("Only one PerFieldPermission allowed for each model "
                                  "permission/field combination.")
