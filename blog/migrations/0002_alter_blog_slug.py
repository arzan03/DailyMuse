# Generated by Django 5.0.6 on 2024-06-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(auto_created=True, unique=True),
        ),
    ]
