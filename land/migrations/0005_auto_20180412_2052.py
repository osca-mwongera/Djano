# Generated by Django 2.0.2 on 2018-04-12 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_auto_20180406_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcel',
            old_name='Area in (Ha)',
            new_name='area',
        ),
    ]
