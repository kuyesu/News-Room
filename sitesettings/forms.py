from django import forms 
from .models import *

class SocialForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Social Platform',
                'class' : 'form-control'
            }
        )
    )
    class Meta:
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'
        model = Social
        fields = "_all_"

class LinkForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Link Name",
                "class" : "form-control"
            }
        )
    )

    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Link URL",
                "class" : "form-control"
            }
        )
    )
    class  Meta:
        model = Link
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class LogoImageForm(forms.Form):
    brand_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Brand Name",
                "class" : "form-control"
            }
        )
    )

    url = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder" : "Logo Image",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = LogoImage
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class AvdvertisementBannerForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Advertisement Name",
                "class" : "form-control"
            }
        )
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder" : "Advertisement Image",
                "class" : "form-control"
            }
        )
    )
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Advertisement URL",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = AvdvertisementBanner
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class SiteNameForm(forms.Form):
    site_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Site Name",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = SiteName
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'