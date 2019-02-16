from django import forms

from .models import User

class UserSignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off'}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off'}))
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off'}))
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
        )

class UserSignInForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off'}))
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
