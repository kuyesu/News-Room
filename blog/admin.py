from django.contrib import admin
from .models import *
from blog.models import Articles
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ('name', 'email', 'website')
    list_filter = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', )
    list_filter = ('name',)

class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('name',)
    list_filter = ('name',)

class ArticleAdmin(admin.TabularInline):
    model = Articles
    list_display = ('title', 'author', 'category', 'status', 'created_time', 'modified_time')
    list_filter = ('title', 'author', 'category', 'status', 'created_time', 'modified_time')

class ArticleInline(admin.TabularInline):
    model = Articles
    extra = 1

# class AvdvertisementBannerAdmin(admin.TabularInline):
#     model = AvdvertisementBanner
#     list_filter = ('name',)
#     list_display = ('name',)

# class IndustryAdmin(admin.TabularInline):
#     model = Industry
#     list_filter = ('name',)

# class SourceAdmin(admin.TabularInline):
#     model = Source
#     list_filter = ('name',)

# class TrendingNewsAdmin(admin.TabularInline):
#     model = TrendingArticle

# class WeeklyArtcileAdmin(admin.TabularInline):
#     model = WeeklyArticle


# class WhatIsNewAdmin(admin.TabularInline):
#     model = WhatIsNew

# class ArticleMediAdmin(admin.TabularInline):
#     model = ArticleMedia


# class ArticleRatingAdmin(admin.TabularInline):
#     model = ArticleRating


# class ArtilcleLikeAdmin(admin.TabularInline):
#     model = ArtilcleLike


# class BookmarkArticleAdmin(admin.TabularInline):
#     model = BookmarkArticle



# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(AvdvertisementBanner, AvdvertisementBannerAdmin)
# admin.site.register(Industry, IndustryAdmin)
# admin.site.register(Source, SourceAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Articles, ArticleAdmin)
# admin.site.register(TrendingArticle, TrendingNewsAdmin)
# admin.site.register(WeeklyArticle, WeeklyArtcileAdmin)
# admin.site.register(WhatIsNew, WhatIsNewAdmin)
# admin.site.register(ArticleMedia, ArticleMediAdmin)
# admin.site.register(ArticleRating, ArticleRatingAdmin)
# admin.site.register(ArtilcleLike, ArtilcleLikeAdmin)
# admin.site.register(BookmarkArticle, BookmarkArticleAdmin)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Industry)
admin.site.register(Source)
admin.site.register(Tag, TagAdmin)
admin.site.register(Articles)
admin.site.register(TrendingArticle)
admin.site.register(WeeklyArticle)
admin.site.register(WhatIsNew)
admin.site.register(ArticleMedia)
admin.site.register(ArticleRating)
admin.site.register(ArtilcleLike)
admin.site.register(BookmarkArticle)