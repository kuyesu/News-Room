from pyexpat import model
from django import forms
from .models import *

class CategoryForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Category Name",
                "class" : "form-control"
            }
        )
    )
    slug = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Category Slug",
                "class" : "form-control"
            }
        )
    )

    class Meta:
        model = Category
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'
    
class TagForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Tag Name",
                "class" : "form-control"
            }
        )
    )
    label = forms.CharField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Tag Label",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = Tag
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class IndustryForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Industry Name",
                "class" : "form-control"
            }
        )
    )
    slug = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Industry Slug",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = Industry
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class SourceForm(forms.Form):
    name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder" : "News Source",
                "class" : "form-control"
            }
        )
    )
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Industry Slug",
                "class" : "form-control"
            }
        )
    )
    active = forms.BooleanField(
        widget= forms.RadioSelect(
            attrs={
                "placeholder" : "Active",
                "class" : "form-control"
            }
        )
    )

    class Meta:
        model = Source
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

