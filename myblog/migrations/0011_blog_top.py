# Generated by Django 3.1.6 on 2021-02-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='top',
            field=models.BooleanField(default=False, verbose_name='是否置顶'),
        ),
    ]
