# Generated by Django 3.1.7 on 2021-03-14 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.task'),
        ),
    ]
