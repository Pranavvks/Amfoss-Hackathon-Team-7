# Generated by Django 3.1.7 on 2021-03-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210314_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Progress',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
