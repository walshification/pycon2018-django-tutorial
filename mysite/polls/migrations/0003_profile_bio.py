# Generated by Django 2.0.4 on 2018-05-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Please enter a bio.', max_length=100),
        ),
    ]