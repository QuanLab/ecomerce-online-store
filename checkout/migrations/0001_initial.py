# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 18:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_auto_20161016_1731'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Submitted'), (2, 'Processed'), (3, 'Shipped'), (4, 'Cancelled')], default=1)),
                ('ip_address', models.GenericIPAddressField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('shipping_name', models.CharField(max_length=50)),
                ('shipping_address_1', models.CharField(max_length=50)),
                ('shipping_address_2', models.CharField(blank=True, max_length=50)),
                ('shipping_city', models.CharField(max_length=50)),
                ('shipping_state', models.CharField(max_length=2)),
                ('shipping_country', models.CharField(max_length=50)),
                ('shipping_zip', models.CharField(max_length=10)),
                ('billing_name', models.CharField(max_length=50)),
                ('billing_address_1', models.CharField(max_length=50)),
                ('billing_address_2', models.CharField(blank=True, max_length=50)),
                ('billing_city', models.CharField(max_length=50)),
                ('billing_state', models.CharField(max_length=2)),
                ('billing_country', models.CharField(max_length=50)),
                ('billing_zip', models.CharField(max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
    ]
