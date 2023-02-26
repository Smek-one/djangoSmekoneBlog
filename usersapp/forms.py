from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Votre pseudo', max_length=20)
    email = forms.EmailField(label='Votre email')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'
    #
    #     self.helper.add_input(Submit('submit', 'Submit'))


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'placeholder': ('Username')
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'first_name',
            'placeholder': ('First Name')
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'last_name',
            'placeholder': ('Last Name')
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'placeholder': ('Email')
        }
    ))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            # 'class':'form-control',
            'placeholder': 'Password'
        }
    ))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            # 'class':'form-control',
            'placeholder': 'Repeat Password'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
