from django.db import models

# Create your models here.

class Social(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class LogoImage(models.Model):
    brand_name = models.CharField(max_length=100)
    url = models.ImageField()

    class Meta:
        verbose_name = "Logo Image"
        verbose_name_plural = "Logo Image"

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name
    
class Slider(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.title

class AvdvertisementBanner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Advertisements"
        verbose_name_plural = "Advertisement"
    def __str__(self):
        return "{}".format(self.name) + "-" + "{}".format(self.updated_at)