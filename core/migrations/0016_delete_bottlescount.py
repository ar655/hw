# Generated by Django 4.1 on 2022-08-27 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_bottlescount_bottle_alter_bottlescount_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BottlesCount',
        ),
    ]
