# Generated by Django 2.1.4 on 2019-01-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190103_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='file_path',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='docs',
            name='screen_vs',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
