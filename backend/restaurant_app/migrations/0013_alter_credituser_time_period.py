# Generated by Django 5.1 on 2024-08-24 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0012_alter_credituser_time_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credituser',
            name='time_period',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 23, 9, 45, 10, 542909, tzinfo=datetime.timezone.utc)),
        ),
    ]
