# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-23 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0002_remove_applicant_preferences'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='preferences',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='applicants.Preferences'),
        ),
    ]