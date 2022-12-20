from django import forms
from .models import Account


class Login(forms.ModelForm):
    class Meta:
        model =Account
        fields =[]

    def __init__(self, arg):
        super(RegistrationForm,forms.ModelForm).__init__()
        self.arg = arg
