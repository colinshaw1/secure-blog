from django import forms
from .models import Post

# class to post form that inherts the model form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'blogger', 'body')
        # add a dictonary for form 
        widgets = {
            # form-control is used for css styling
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'blogger': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }