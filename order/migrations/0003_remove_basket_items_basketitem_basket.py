# Generated by Django 5.1.5 on 2025-04-09 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='items',
        ),
        migrations.AddField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.basket'),
            preserve_default=False,
        ),
    ]
