# Generated by Django 3.0.6 on 2020-06-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200604_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='registrations',
        ),
        migrations.AddField(
            model_name='event',
            name='registrations',
            field=models.IntegerField(default=0),
        ),
    ]
