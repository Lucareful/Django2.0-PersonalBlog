# Generated by Django 2.1.2 on 2019-01-22 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_page_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url_image',
        ),
    ]