# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-02-09 11:08
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo1',
            field=models.ImageField(upload_to='item/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='item/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='item/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_image',
            field=models.ImageField(upload_to='avatar/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_logo',
            field=models.ImageField(upload_to='store-logo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format: '+234...'. Up to 13 digits allowed.", regex='^\\+?234?\\d{10}$')]),
        ),
    ]
