# Generated by Django 3.2.4 on 2021-07-01 15:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_articlepost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 1, 15, 46, 4, 915690, tzinfo=utc)),
        ),
    ]