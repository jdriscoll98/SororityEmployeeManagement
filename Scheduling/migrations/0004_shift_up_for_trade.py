# Generated by Django 2.1.4 on 2019-01-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scheduling', '0003_auto_20190101_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='up_for_trade',
            field=models.BooleanField(default=False),
        ),
    ]