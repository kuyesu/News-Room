from django.db import models
from userauth.models import CustomUser as User
from blog.models import Articles
from django.urls import reverse
# Create your models here.
from ckeditor.fields import RichTextField
class Comment(models.Model):
    article = models.ForeignKey(Articles, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    body = RichTextField()
    website = models.URLField(blank=True)
    created_time = models.DateTimeField()
    
    def __str__(self):
        return "{}".format(self.user) + " - " + "{}".format(self.created_time)

    class Meta:
        ordering = ['-created_time']

    # def get_absolute_url(self):
    #     return reverse('article-detail', kwargs={"pk": self.pk})


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     comment = models.TextField(max_length=400)
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return self.comment[:60]