# Generated by Django 3.2.12 on 2022-05-23 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite_movies',
        ),
    ]
