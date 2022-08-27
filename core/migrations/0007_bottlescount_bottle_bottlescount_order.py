# Generated by Django 4.1 on 2022-08-27 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_order'),
        ('core', '0006_bottlescount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottlescount',
            name='bottle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottlescount', to='core.botlle'),
        ),
        migrations.AddField(
            model_name='bottlescount',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottlescount', to='clients.order'),
        ),
    ]
