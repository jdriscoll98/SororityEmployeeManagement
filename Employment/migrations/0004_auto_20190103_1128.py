# Generated by Django 2.1.4 on 2019-01-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employment', '0003_auto_20190103_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clock',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
