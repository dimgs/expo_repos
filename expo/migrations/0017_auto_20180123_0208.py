# Generated by Django 2.0 on 2018-01-23 01:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expo', '0016_painting_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painting',
            name='created_date',
        ),
        migrations.AddField(
            model_name='painting',
            name='created_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2018)]),
        ),
        migrations.AlterField(
            model_name='painting',
            name='counter_popularity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='painting',
            name='rating',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='painting',
            name='status',
            field=models.CharField(choices=[('online', 'On'), ('offline', 'Off')], default='on', max_length=8),
        ),
    ]
