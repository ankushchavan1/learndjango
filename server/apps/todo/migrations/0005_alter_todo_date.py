# Generated by Django 3.2.6 on 2021-08-16 07:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210816_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
