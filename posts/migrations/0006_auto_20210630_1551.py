# Generated by Django 3.2.3 on 2021-06-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_conversa_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_subtitle',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]