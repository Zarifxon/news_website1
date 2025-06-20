# Generated by Django 5.2.3 on 2025-06-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0018_remove_news_language_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='body_uz',
            field=models.TextField(null=True),
        ),
    ]
