from django import forms 

from .models import Comment

class CommentForm(forms.Form):
    user = forms.CharField(
        label='Name',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Name"
            }
        )
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Email"
            }
        )
    )
    body = forms.CharField(
        label='Comment',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Comment"
            }
        )
    )
    website = forms.URLField(
        label='Website',
        required=False,
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Website"
            }
        )
    )

    post = forms.CharField(widget=forms.HiddenInput())



    class Meta:
        model = Comment
        fields = ['user', 'email', 'body', 'website']




    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body) < 10:
            raise forms.ValidationError('Comment is too short.')
        return body

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)