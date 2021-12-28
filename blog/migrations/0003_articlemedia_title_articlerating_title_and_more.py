# Generated by Django 4.0 on 2021-12-26 13:18

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemedia',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='articlerating',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='artilclelike',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='bookmarkarticle',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='industry',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='relatedarticle',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='trendingarticle',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='weeklyarticle',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='whatisnew',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
        migrations.AddField(
            model_name='whatisnew',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relatedarticle',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_article', to='blog.source'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='whatisnew',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
