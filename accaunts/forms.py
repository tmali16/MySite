from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Не правельный логин или пароль")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Имя полльзователя")
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Repeat Email')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'password2'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        username = self.cleaned_data.get('username')
        if email != email2:
            raise forms.ValidationError("E-mail не воспадает")
        email_as=User.objects.filter(email=email)
        if email_as.exists():
            raise forms.ValidationError("Данный E-mail уже используется")

        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароль не воспадает")
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("Данное имя пользователя используется, выберите другую")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
