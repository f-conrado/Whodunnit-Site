# Generated by Django 3.2.3 on 2021-06-15 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210610_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_title',
        ),
    ]
