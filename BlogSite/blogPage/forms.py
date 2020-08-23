from django import forms
from .models import Post, Category

category_choices = Category.objects.all().values_list('name','name')
category_list = []
for item in category_choices:
    category_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title here...'}),  #form control is a bootstrap class
            'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=category_list, attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter the content here...'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title here...'}),  #form control is a bootstrap class
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter the content here...'}),
            'category' : forms.Select(choices=category_list, attrs={'class':'form-control'}),
        }
