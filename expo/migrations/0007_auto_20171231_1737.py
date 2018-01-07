# Generated by Django 2.0 on 2017-12-31 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expo', '0006_auto_20171231_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='f_ancestry',
        ),
        migrations.RemoveField(
            model_name='museum',
            name='f_country',
        ),
        migrations.AddField(
            model_name='artist',
            name='f_city',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='expo.City'),
        ),
        migrations.AddField(
            model_name='museum',
            name='f_city',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='expo.City'),
        ),
        migrations.DeleteModel(
            name='Ancestry',
        ),
    ]
