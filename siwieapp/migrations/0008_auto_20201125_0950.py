# Generated by Django 3.1.3 on 2020-11-25 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siwieapp', '0007_auto_20201125_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logbook',
            old_name='owner',
            new_name='user',
        ),
    ]