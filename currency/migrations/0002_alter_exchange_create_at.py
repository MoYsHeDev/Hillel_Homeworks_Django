# Generated by Django 3.2.7 on 2021-09-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
