# Generated by Django 4.2.3 on 2023-07-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jahanvi', '0002_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
