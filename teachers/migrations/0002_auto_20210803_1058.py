# Generated by Django 3.2.5 on 2021-08-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='discipline',
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=23),
        ),
    ]