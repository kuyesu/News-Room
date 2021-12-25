from django import forms
from .models import Code

class CodeForm(forms.Form):
    number = forms.CharField(label="Code", help_text="Enter the SMS verification code")
    class Meta:
        model = Code
        fields = ("number",)