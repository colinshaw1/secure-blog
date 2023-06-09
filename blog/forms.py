from django import forms
from .models import Post, Comments

# class to post form that inherts the model form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'blogger', 'body')
        # add a dictonary for form 
        widgets = {
            # form-control is used for css styling
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Please enter a title for you blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Please enter a blog tag'}),
            'blogger': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Please enter your blog post here :)'}),
        }

# class to post form that inherts the model form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body',)
        # add a dictonary for form 
        widgets = {
            # form-control is used for css styling
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Please enter your name for your comment'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Please enter your blog post here :)'}),
        }