from django import forms

from .models import User

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'date_of_birth',
            'email',
        )
