# Generated by Django 4.0 on 2021-12-27 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('blog', '0004_rename_title_author_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comment'),
        ),
    ]
