from django import forms
from .models import Post, Category, Comment

#choices = [('Coding', 'Coding'),('Philosophy','Philosophy'),('Personal','Personal'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'author', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title tag'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Pick a category'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Pick an author'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your body text'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'header_image') #'author',

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title tag'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Pick a category'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your body text'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a comment'}),
        }
