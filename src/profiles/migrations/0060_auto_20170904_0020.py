# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0059_profile_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='parent_email',
            new_name='father_email',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='student_phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
