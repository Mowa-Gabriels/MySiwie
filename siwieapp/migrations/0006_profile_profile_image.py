# Generated by Django 2.2.7 on 2020-11-16 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siwieapp', '0005_remove_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='he.png', null=True, upload_to='user/'),
        ),
    ]
