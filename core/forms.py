from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'message'
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
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'cols' : 30,
                'rows' : 5,
                'placeholder' : 'Your message'
            })
        }
    
    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')  
        if value:
            return value.lower()
        return value
    

    def clean(self):
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
            raise forms.ValidationError('Email is not accepted. Please enter gmail address!')
        return self.cleaned_data
    

