# Generated by Django 4.0.2 on 2022-02-27 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstblog', '0009_profile_linkedin_url_profile_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='body',
            new_name='bio',
        ),
    ]
