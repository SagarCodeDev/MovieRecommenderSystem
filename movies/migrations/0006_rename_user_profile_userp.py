# Generated by Django 4.1.1 on 2022-10-09 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='userp',
        ),
    ]
