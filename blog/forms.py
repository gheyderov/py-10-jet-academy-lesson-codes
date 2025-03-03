from django import forms
from blog.models import Blog, BlogCategory


class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'image',
            'category'
        )
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'rows' : 3
            }),
            'category' : forms.Select(attrs={
                'class' : 'form-control'
            })
        }