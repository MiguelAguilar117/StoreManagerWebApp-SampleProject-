from django import forms
from .models import StoreManager

class StoreManagerSignUp_Form(forms.ModelForm):
    class Meta:
        model = StoreManager
        fields = ['firstname', 'lastname', 'password', 'email']

class StoreManagerLogin_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)