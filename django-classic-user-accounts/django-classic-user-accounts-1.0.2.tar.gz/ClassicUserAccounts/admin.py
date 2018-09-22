from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, RegistrationForm
from .models import User


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = RegistrationForm
    
    list_display = ('avatar_tag', 'get_full_name', 'email', 'mobile', 'website', 'is_admin')
    list_filter = ('email', 'first_name')
    fieldsets = (
        (None, {'fields': ('email', )}),
        ('Personal Info', {'fields': ('avatar', 'title', 'first_name', 'last_name', 'date_of_birth', 'gender',
                                      'business_email', 'timezone')}),
        ('Contact info', {'fields': ('mobile', 'website')}),
        ('Social info', {'fields': ('skype_id', 'facebook_id', 'linkedin_id', 'twitter_id')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_admin', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    # readonly_fields = ('email',)
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2')}
    #     ),
    # )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal Info', {'fields': ('avatar', 'title', 'first_name', 'last_name', 'date_of_birth')}),
        ('Contact info', {'fields': ('mobile', 'website')}),
        ('Social info', {'fields': ('skype_id', 'facebook_id', 'linkedin_id', 'twitter_id')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_admin', 'groups', 'user_permissions')}),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)