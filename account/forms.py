from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class ProfileForm(forms.ModelForm):

    full_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))

    class Meta:
        model = User
        fields = (
            'email',
            'phone'
        )
        widgets = {
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control'
            }),
            'phone' : forms.TextInput(attrs={
                'class' : 'form-control'
            })
        }

    def save(self, commit = ...):
        full_name = self.cleaned_data['full_name']
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        self.instance.first_name = first_name
        self.instance.last_name = last_name
        return super().save(commit)


class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
            'password'
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'First Name'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Last Name'
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email'
            }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'
            }),
        }

    def save(self, commit = ...):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()
        return user

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match!')
        return super().clean()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username'
    }))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password'
    }))
