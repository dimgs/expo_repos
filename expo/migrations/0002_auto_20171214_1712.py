# Generated by Django 2.0 on 2017-12-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='artist',
            field=models.CharField(max_length=50),
        ),
    ]
