# Generated by Django 3.1.6 on 2021-02-08 14:55

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20210208_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='文章内容'),
        ),
    ]
