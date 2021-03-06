# Generated by Django 3.1.7 on 2021-04-27 04:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20210427_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='tags',
            new_name='sun_forum',
        ),
        migrations.AlterField(
            model_name='query',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='reply',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
