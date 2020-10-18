# Generated by Django 3.0.7 on 2020-10-18 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20201018_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='movieactor',
            old_name='actor_id',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='movieactor',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='moviedirector',
            old_name='director_id',
            new_name='director',
        ),
        migrations.RenameField(
            model_name='moviedirector',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
