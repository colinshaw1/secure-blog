from django import forms
froom .models import Post

# class to post form that inherts the model form
class PostForm(forms.ModelForm):
    class Meta:
    model = Post
    fields = ('title', 'slug', 'blogger', 'body')
    # add a dictonary for form 
    widget = {
        # form-control is used for css styling
        'title': form.TextInput(attrs={'class':'form-control'})
        'slug': form.TextInput(attrs={'class':'form-control'})
        'blogger': form.Select(attrs={'class':'form-control'})
        'body': form.Textarea(attrs={'class':'form-control'})
    }