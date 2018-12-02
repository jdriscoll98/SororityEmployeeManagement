# Generated by Django 2.0 on 2018-10-15 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20181015_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='available_shifts',
            field=models.ManyToManyField(blank=True, to='website.AvailableShift'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='scheduled_shifts',
            field=models.ManyToManyField(blank=True, to='website.ScheduledShift'),
        ),
    ]
