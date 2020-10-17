# Generated by Django 3.0.7 on 2020-10-16 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20201016_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='reservation_rate',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='movie',
            name='grade',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
    ]