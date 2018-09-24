from .models import Configuration
from django import forms
from django.forms import ModelForm, PasswordInput

class AdminForm(ModelForm):
    token = forms.CharField(widget=PasswordInput())
    class Meta:
        model = Configuration
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)