# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-05 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('publicbody', '0010_auto_20171225_0633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='classification',
            options={'verbose_name': 'classification', 'verbose_name_plural': 'classifications'},
        ),
        migrations.AlterField(
            model_name='categorizedpublicbody',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorized_publicbodies', to='publicbody.Category'),
        ),
        migrations.AlterField(
            model_name='publicbody',
            name='categories',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='publicbody.CategorizedPublicBody', to='publicbody.Category', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='publicbody',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publicbody.Classification'),
        ),
    ]
