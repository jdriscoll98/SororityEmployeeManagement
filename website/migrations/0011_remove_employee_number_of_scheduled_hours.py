# Generated by Django 2.0 on 2018-10-21 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='number_of_scheduled_hours',
        ),
    ]
