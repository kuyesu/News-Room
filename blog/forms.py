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

class AUthorForm(forms.Form):
    name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder" : "Author Name",
                "class" : "form-control"
            }
        )
    )
    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder" : "Author Photo",
                "class" : "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Author Email",
                "class" : "form-control"
            }
        )
    )
    website = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Author Website",
                "class" : "form-control"
            }
        )
    )

    class Meta:
        model = Author
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class ArticlesForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Article Title",
                "class" : "form-control"
            }
        )
    )
    source = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Source",
                "class" : "form-control"
            }
        ),
        queryset=Source.objects.all()
    )
    category = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Category",
                "class" : "form-control"
            }
        ),
        queryset=Category.objects.all()
    )
    tags = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={
                "placeholder" : "Article Tags",
                "class" : "form-control"
            }
        ),
        queryset=Tag.objects.all()
    )
    industry = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Industry",
                "class" : "form-control"
            }
        ),
        queryset=Industry.objects.all()
    )
    
    author = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Author",
                "class" : "form-control"
            }
        ),
        queryset=Author.objects.all()
    )
    cover_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder" : "Article Cover Image",
                "class" : "form-control"
            }
        )
    )
    cover_introduction = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Article Cover Introduction",
                "class" : "form-control"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Article Content",
                "class" : "form-control"
            }
        )
    )
    created_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder" : "Article Created Time",
                "class" : "form-control"
            }
        )
    )
    modified_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder" : "Article Modified Time",
                "class" : "form-control"
            }
        )
    )
    status = forms.BooleanField(
        widget=forms.RadioSelect(
            attrs={
                "placeholder" : "Article Status",
                "class" : "form-control"
            }
        )
    )
    avg_rating = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Article Avg Rating",
                "class" : "form-control"
            }
        )
    )
    view_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Article View Count",
                "class" : "form-control"
            }
        )
    )
    rating_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Article Rating Count",
                "class" : "form-control"
            }
        )
    )
    slug = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Article Slug",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = Articles
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'
    
class TrendingArticleForm(forms.Form):
    Articles = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Trending Article",
                "class" : "form-control"
            }
        ),
        queryset=Articles.objects.all()
    )
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder" : "Trending Time",
                "class" : "form-control"
            }
        )
    )
    updated_at = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder" : "Trending Time",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = TrendingArticle
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class WeeklyArticleForm(forms.Form):
    Articles = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Weekly Article",
                "class" : "form-control"
            }
        ),
        queryset=Articles.objects.all()
    )
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder" : "Weekly Time",
                "class" : "form-control"
            }
        )
    )
    updated_at = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder" : "Weekly Time",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = WeeklyArticle
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class WhatIsNewForm(forms.Form):
    author = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "What Is New Author",
                "class" : "form-control"
            }
        ),
        queryset=Author.objects.all()
    )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Article Title",
                "class" : "form-control"
            }
        )
    )
    
    category = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Category",
                "class" : "form-control"
            }
        ),
        queryset=Category.objects.all()
    )
    tags = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={
                "placeholder" : "Article Tags",
                "class" : "form-control"
            }
        ),
        queryset=Tag.objects.all()
    )
    industry = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Industry",
                "class" : "form-control"
            }
        ),
        queryset=Industry.objects.all()
    )
    
    author = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Author",
                "class" : "form-control"
            }
        ),
        queryset=Author.objects.all()
    )
    cover_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder" : "Article Cover Image",
                "class" : "form-control"
            }
        )
    )
    cover_introduction = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Article Cover Introduction",
                "class" : "form-control"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Article Content",
                "class" : "form-control"
            }
        )
    )
    created_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder" : "Article Created Time",
                "class" : "form-control"
            }
        )
    )
    modified_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder" : "Article Modified Time",
                "class" : "form-control"
            }
        )
    )
    status = forms.BooleanField(
        widget=forms.RadioSelect(
            attrs={
                "placeholder" : "Article Status",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = WhatIsNew
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class ArticleMediaForm(forms.Form):
    article = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Media",
                "class" : "form-control"
            }
        ),
        queryset=Articles.objects.all()
    )
    category = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Media",
                "class" : "form-control"
            }
        ),
        queryset=Category.objects.all()
    )
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Article Media",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = ArticleMedia
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class ArticleRatingForm(forms.Form):
    article = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Rating",
                "class" : "form-control"
            }
        ),
        queryset=Articles.objects.all()
    )
    rating = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Article Rating",
                "class" : "form-control"
            }
        )
    )
    user = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Rating",
                "class" : "form-control"
            }
        ),
        queryset=User.objects.all()
    )

    class Meta:
        model = ArticleRating
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class RelatedArticleForm(forms.Form):
    source = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Related Article",
                "class" : "form-control"
            }
        ),
        queryset=Source.objects.all()
    )
    related = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Related Article",
                "class" : "form-control"
            }
        ),
        queryset=Articles.objects.all()
    )
    score = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Related Article",
                "class" : "form-control"
            }
        )
    )
    class Meta:
        model = RelatedArticle
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class ArticleLikeForm(forms.Form):
    article = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Like",
                "class" : "form-control"
            }
        ),
        queryset=Articles.objects.all()
    )
    user = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Article Like",
                "class" : "form-control"
            }
        ),
        queryset=User.objects.all()
    )
    is_like = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Article Like",
                "class" : "form-control"
            }
        )
    )

    class Meta:
        model = ArtilcleLike
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class BookmarkArticleForm(forms.Form):
    article = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Bookmark Article",
                "class" : "form-control"
            }
        ),
        queryset=Articles.objects.all()
    )
    user = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder" : "Bookmark Article",
                "class" : "form-control"
            }
        ),
        queryset=User.objects.all()
    )
    class Meta:
        model = BookmarkArticle
        field = "_all_"
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'

class FeedForm(forms.Form):
    pass