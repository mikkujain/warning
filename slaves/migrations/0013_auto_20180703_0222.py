# Generated by Django 2.0 on 2018-07-03 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slaves', '0012_auto_20180703_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='default_expiry_time',
            field=models.IntegerField(verbose_name='Time to wait for next alert in minutes'),
        ),
    ]
