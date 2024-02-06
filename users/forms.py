from django import forms
from users.models import Users
from django.core.exceptions import ValidationError


class AddRegisterUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control', 'type': 'password'
            })
        }

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