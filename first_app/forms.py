from urllib import request
from django import forms
from first_app.models import User

class LoggingForm(forms.ModelForm):
    verify_email = forms.EmailField(label='Enter your email again: ')
    class Meta:
        model = User
        fields = '__all__'
