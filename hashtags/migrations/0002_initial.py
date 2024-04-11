# Generated by Django 5.0.3 on 2024-04-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hashtags', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ManyToManyField(related_name='hashtags', to='posts.post'),
        ),
    ]