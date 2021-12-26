from django import forms 
from .models import *

class MenuForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Menu Title",
                "class" : "form-control"
            }
        )
    )
    slug = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Menu Slug",
                "class" : "form-control"
            }
        )
    )
    
    class Meta:
        model = Menu
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class MenuItemForm(forms.Form):
    menu = forms.ModelChoiceField(
        queryset=Menu.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder" : "Menu",
                "class" : "form-control"
            }
        )
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Menu Item Title",
                "class" : "form-control"
            }
        )
    )
    link_url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Link URL",
                "class" : "form-control"
            }
        )
    )
    link_Articles = forms.ModelChoiceField(
        queryset=Articles.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder" : "Link Articles",
                "class" : "form-control"
            }
        )
    )

    title_of_submenu = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Title of Submenu",
                "class" : "form-control"
            }
        )
    )
    icon = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder" : "Icon",
                "class" : "form-control"
            }
        )
    )
    show_when = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Show When",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = MenuItem
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'