# Generated by Django 2.1.2 on 2019-01-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='cover',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
