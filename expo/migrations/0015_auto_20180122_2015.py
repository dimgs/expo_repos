# Generated by Django 2.0 on 2018-01-22 19:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('expo', '0014_auto_20180122_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famous',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Mona Lisa', 'Mona Lisa'), ('Starry Night', 'Starry Night'), ('The Last Supper', 'The Last Supper'), ('The Creation of Adam', 'The Creation of Adam'), ('Guernica', 'Guernica')], max_length=68),
        ),
    ]
