from distutils.command.upload import upload
from random import choice
from telnetlib import STATUS
from django.db import models

# Create your models here.

class Social(models.Model):
    title = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    url = models.URLField()

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __str__(self):
        return self.name

class Link(models.Model):
    CHOICE = (
        ('1', 'Facebook'),
        ('2', 'Twitter'),
        ('3', 'Instagram'),
        ('4', 'Youtube'),
        ('5', 'Linkedin'),
        ('6', 'Google'),
        ('7', 'Pinterest'),
    )
    title = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    url = models.URLField()

    def __str__(self):
        return self.name

class LogoImage(models.Model):
    brandlogo = models.ImageField(upload_to='images/', null=True, blank=False)
    brand_name = models.CharField(max_length=100, null=True, blank=False)
    

    class Meta:
        verbose_name = "Logo Image"
        verbose_name_plural = "Logo Image"

    def __str__(self):
        return self.brand_name

class Video(models.Model):
    title = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    url = models.URLField()

    def __str__(self):
        return self.name
    
class Slider(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    body = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.title

class AdvertisementBanner(models.Model):
    STATUS = (
        ('Top Banner', 'Top Banner'),
        ('On side', 'On side')
    )
    where_to_locate = models.CharField(choices=STATUS, blank=False, null=True, max_length=12)
    name = models.CharField(max_length=100, null=True, blank=False)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Advertisement (Ads)"
        verbose_name_plural = "Advertisement (Ads)"
    def __str__(self):
        return "{}".format(self.name) + "-" + "{}".format(self.updated_at)

    

class SiteName(models.Model):
    title = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title