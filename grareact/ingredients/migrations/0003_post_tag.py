# Generated by Django 3.0.8 on 2020-07-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='ingredients.Tag'),
        ),
    ]