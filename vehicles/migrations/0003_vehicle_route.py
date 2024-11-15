# Generated by Django 5.1.2 on 2024-10-23 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0004_remove_route_vehicles'),
        ('vehicles', '0002_vehicle_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicles', to='routes.route'),
        ),
    ]
