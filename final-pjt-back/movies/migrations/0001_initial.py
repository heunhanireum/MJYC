# Generated by Django 3.2.12 on 2022-05-24 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_num', models.IntegerField()),
                ('rank', models.FloatField()),
                ('content', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('overview', models.TextField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('genres', models.CharField(max_length=100, null=True)),
                ('movie_num', models.IntegerField(null=True)),
                ('like_count', models.IntegerField(default=0)),
                ('movie_like', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
