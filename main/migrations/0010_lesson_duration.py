# Generated by Django 3.2.4 on 2021-06-23 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_course_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=1200)),
        ),
    ]