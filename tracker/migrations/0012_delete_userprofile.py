# Generated by Django 4.2.11 on 2024-04-21 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_alter_userprofile_timezone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
