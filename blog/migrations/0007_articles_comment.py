# Generated by Django 4.0 on 2021-12-27 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_remove_comment_article'),
        ('blog', '0006_remove_articles_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comment'),
        ),
    ]
