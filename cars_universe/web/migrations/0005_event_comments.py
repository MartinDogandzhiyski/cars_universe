# Generated by Django 4.2.2 on 2023-06-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='comments',
            field=models.ManyToManyField(related_name='event_comments', to='web.comment'),
        ),
    ]
