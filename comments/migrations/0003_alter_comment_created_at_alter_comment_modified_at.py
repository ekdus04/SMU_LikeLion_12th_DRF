# Generated by Django 5.0.3 on 2024-04-08 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_created_at_alter_comment_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 15, 46, 48, 432787, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 15, 46, 48, 432787, tzinfo=datetime.timezone.utc)),
        ),
    ]
