# Generated by Django 4.1 on 2022-08-27 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_bottlescount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botlle',
            name='orders',
        ),
    ]
