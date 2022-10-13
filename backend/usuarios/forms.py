from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile


class LoginForm( forms.Form):
    email = forms.CharField(
        required=True,
        label='Email do usuário',
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'}), label='Senha')


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='Email do usuário',
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))


class RecoverPassword(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha atual'}),
        label='Senha')
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repitir a nova senha'}),
        label='Repitir a nova senha')


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        repeat_password = cleaned_data['repeat_password']
        if repeat_password != password:
            raise ValidationError(
                {"repeat_password": "Senha não confirma, corrija e tente novamente."}
            )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        label='Primeiro nome',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Primeiro nome'})
    )
    last_name = forms.CharField(
        max_length=50,
        label='Ultimo nome',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Último nome'})
    )
    email = forms.CharField(
        required=True,
        label='Email do usuário',
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'})
    )
    
    phone_number = forms.CharField(
        max_length=15,
        label='Telefone',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Telefone'})
    )
    username = forms.CharField(
        max_length=50,
        label='Nome de usuário',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome de usuário'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'}),
        label='Senha')
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repitir senha'}),
        label='Repitir senha')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        repeat_password = cleaned_data['repeat_password']
        if repeat_password != password:
            raise ValidationError(
                {"repeat_password": "Senha não confirma, corrija e tente novamente."}
            )
    

class ChangerPassword(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha atual'}),
        label='Senha')
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Nova senha'}),
        label='Nova senha')
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repitir a nova senha'}),
        label='Repitir a nova senha')


    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data['new_password']
        repeat_password = cleaned_data['repeat_password']
        if repeat_password != new_password:
            raise ValidationError(
                {"repeat_password": "Senha não confirma, corrija e tente novamente."}
            )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'profile_picture',
            'cover_photo',
            'address_line_1',
            'address_line_2',
            'country',
            'state',
            'city',
            'pin_code',
            'latitude',
            'longitude')