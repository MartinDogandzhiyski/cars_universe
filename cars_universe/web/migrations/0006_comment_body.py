# Generated by Django 4.2.2 on 2023-06-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_event_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default=''),
        ),
    ]