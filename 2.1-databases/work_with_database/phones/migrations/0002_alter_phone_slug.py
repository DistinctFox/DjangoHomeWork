# Generated by Django 5.0.6 on 2024-05-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=80),
        ),
    ]
