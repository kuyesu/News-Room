# Generated by Django 4.0 on 2021-12-25 16:10

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='Unique identifier of menu. Will be populated automatically from title of menu. Change only if needed.', populate_from='title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, db_index=True)),
                ('title', models.CharField(blank=True, help_text='Title of menu item that will be displayed', max_length=50, null=True)),
                ('link_url', models.CharField(blank=True, help_text='URL to link to, e.g. /accounts/signup (no language prefix, LEAVE BLANK if you want to link to a page instead of a URL)', max_length=500, null=True)),
                ('title_of_submenu', models.CharField(blank=True, help_text='Title of submenu (LEAVE BLANK if there is no custom submenu)', max_length=50, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('show_when', models.CharField(choices=[('always', 'Always'), ('logged_in', 'When logged in'), ('not_logged_in', 'When not logged in')], default='always', max_length=15)),
                ('link_Articles', models.ForeignKey(blank=True, help_text='Page to link to (LEAVE BLANK if you want to link to a URL instead)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.articles')),
                ('menu', modelcluster.fields.ParentalKey(help_text='Menu to which this item belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menu.menu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
