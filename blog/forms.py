from pyexpat import model
from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = "__all__"

