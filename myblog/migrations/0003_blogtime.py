# Generated by Django 2.1.2 on 2018-10-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20181010_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('time_title', models.CharField(max_length=150)),
                ('things', models.TextField()),
            ],
        ),
    ]
