from django.db import models
from blog.models import Articles
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_time = models.DateTimeField()
    post = models.ForeignKey(Articles, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.created_time

    class Meta:
        ordering = ['-created_time']