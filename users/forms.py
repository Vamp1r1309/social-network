from django import forms
from users.models import User
from django.core.exceptions import ValidationError


class AddRegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name',
            'username', 'password']
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
                'type': 'email',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control', 
                'type': 'password'
            })
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        from validate_email import validate_email
        is_valid = validate_email(email, verify=True)
        if not is_valid:
            raise ValidationError("Email не существует")
        return email


    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise ValidationError("Длина пароля должна быть более 6 символов")
        if len(username) > 50:
            raise ValidationError("Длина имени превышает 50 символов")
        return username
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError("Длина пароля должна быть более 8 символа")
        return password