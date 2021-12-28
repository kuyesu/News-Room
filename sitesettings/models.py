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
    title = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    url = models.URLField()

    def __str__(self):
        return self.name

class LogoImage(models.Model):
    title = models.CharField(max_length=70, null=True, blank=False)
    brand_name = models.CharField(max_length=100, null=True, blank=False)
    url = models.ImageField()

    class Meta:
        verbose_name = "Logo Image"
        verbose_name_plural = "Logo Image"

    def __str__(self):
        return self.name

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

class AvdvertisementBanner(models.Model):
    
    name = models.CharField(max_length=100, null=True, blank=False)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Advertisements"
        verbose_name_plural = "Advertisement"
    def __str__(self):
        return "{}".format(self.name) + "-" + "{}".format(self.updated_at)


class SiteName(models.Model):
    title = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title