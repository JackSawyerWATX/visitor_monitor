# Generated by Django 2.2.28 on 2023-11-19 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]