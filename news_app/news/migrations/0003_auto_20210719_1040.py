# Generated by Django 3.2.5 on 2021-07-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_links',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_link',
            field=models.CharField(max_length=300),
        ),
    ]