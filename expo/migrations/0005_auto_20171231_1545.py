# Generated by Django 2.0 on 2017-12-31 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expo', '0004_auto_20171230_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='f_ancestry_id',
            new_name='f_ancestry',
        ),
        migrations.RenameField(
            model_name='painting',
            old_name='f_artist_id',
            new_name='f_artist',
        ),
        migrations.RenameField(
            model_name='painting',
            old_name='f_genre_id',
            new_name='f_genre',
        ),
        migrations.RenameField(
            model_name='painting',
            old_name='f_museum_id',
            new_name='f_museum',
        ),
        migrations.RenameField(
            model_name='painting',
            old_name='f_period_id',
            new_name='f_period',
        ),
    ]
