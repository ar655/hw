# Generated by Django 4.1 on 2022-08-27 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_order_options_order_client_alter_order_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
    ]
