from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from django.urls import reverse

from userauth.models import CustomUser as User
# from comments.models import Comment
from ckeditor.fields import RichTextField


# Create your models here.


class NewsSiteBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True

# blog category
class Category(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    slug = models.SlugField(
        null=True,
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify posts by this category',
    )

    class Meta:
        
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Tag(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    
    LABEL = (
        ('warning', 'warning'),
        ('danger', 'danger'),
        ('primary', 'primary'),
        ('dark', 'dark'),
        ('gray', 'gray'),
        ('orange', 'orange'),
    )
 
    label = models.CharField(choices=LABEL, null=True, max_length=10)

    def __str__(self):
        return self.name

    
class Industry(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    slug = models.SlugField(
        null=True,
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify Articless by this Industry',
    )

    class Meta:
        
        verbose_name_plural = "Industries"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Source(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    url = models.URLField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Author(models.Model):
    message = models.CharField(max_length=70, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Articles(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    industry = models.ForeignKey(Industry, blank=True, null=True, default=None, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    cover_introduction = models.TextField(null=True, blank=False)
    content = RichTextUploadingField(null=True, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    STATUS = (("Draft", 'Draft'), ("Published", 'Published'))
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    avg_rating = models.FloatField(blank=True, null=True)
    view_count = models.FloatField(blank=True, null=True)
    rating_count = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return "{}".format(self.title) + " - " + "{}".format(self.created_time) + " - " + "{}".format(self.author)

    @property
    def imageURL(self):
        try:
            url = self.cover_image.url
        except:
            url=''
        return url

    # def get_absolute_url(self):
    #     return reverse('article-detail', kwargs={'slug':self.slug, 'id':self.id})

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    


class TrendingArticle(models.Model):
    title = models.CharField(max_length=70, null=True, blank=False)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="treding_post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS = (("List", 'List'), ("Top", 'Top'))
    status_choice = models.CharField(max_length=10, choices=STATUS, null=True, default="List")

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Trending Articles"
    def __str__(self):
        return "{}".format(self.articles) + " - " + "{}".format(self.updated_at) + "{}".format(self.title)


class WeeklyArticle(models.Model):
    title = models.CharField(max_length=70, null=True, blank=False)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Weekley Articles"

    def __str__(self):
        return "{}".format(self.articles) + " - " + "{}".format(self.updated_at)

class RecentArticle(models.Model):
    title = models.CharField(max_length=70, null=True, blank=False)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Recent Articles"

    def __str__(self):
        return "{}".format(self.articles) + " - " + "{}".format(self.updated_at)


class WhatIsNew(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, )
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    industry = models.ForeignKey(Industry, blank=True, null=True, default=None, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    cover_introduction = models.TextField(null=True, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    STATUS = (("Draft", 'Draft'), ("Published", 'Published'))
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    content = RichTextUploadingField(null=True, blank=False)

    def __str__(self):
        return "{}".format(self.title) + " - " + "{}".format(self.created_time) + " - " + "{}".format(self.category)

    class Meta:
        ordering = ['-created_time']
        verbose_name = "What is new"
        verbose_name_plural = "What is new"

    @property
    def imageURL(self):
        try:
            url = self.cover_image.url
        except:
            url=''
        return url

class ArticleMedia(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return "{}".format(self.article) + " - " + "{}".format(self.category)
    
    class Meta:
        verbose_name_plural = "Article Media"


# TODO: add reference to User model
class ArticleRating(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return "{}".format(self.article) + " - " + "{}".format(self.user)
    class Meta:
        verbose_name_plural = "Article Ratings"


class RelatedArticle(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    source = models.ForeignKey(Source, related_name="source_article", on_delete=models.CASCADE)
    related = models.ForeignKey(Articles, related_name="related_article", on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return "{}".format(self.source) + " - " + "{}".format(self.related)

    class Meta:
        verbose_name_plural = "Related Articles"

class ArtilcleLike(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    is_like = models.PositiveSmallIntegerField(default=2)

    def __str__(self):
        return "{}".format(self.user) + " - " + "{}".format(self.article)
    class Meta:
        verbose_name_plural = "Article Likes"


class BookmarkArticle(NewsSiteBaseModel):
    title = models.CharField(max_length=70, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.user) + " - " + "{}".format(self.article)
    class Meta:
        verbose_name_plural = "Bookmark Articles"


class Feed:
    pass