# Generated by Django 3.1.6 on 2021-02-09 02:39

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_auto_20210208_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', mdeditor.fields.MDTextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '关于',
                'verbose_name_plural': '关于',
            },
        ),
    ]