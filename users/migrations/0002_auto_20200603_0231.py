# Generated by Django 3.0.6 on 2020-06-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creator',
            name='mobile',
        ),
        migrations.AlterField(
            model_name='creator',
            name='gmail_email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Google Email'),
        ),
    ]
