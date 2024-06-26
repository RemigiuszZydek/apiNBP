# Generated by Django 5.0.6 on 2024-06-08 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('date', models.DateField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiPostgreSQL.currency')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('currency', 'date')},
            },
        ),
        migrations.CreateModel(
            name='ExchangeRateArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('date', models.DateField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiPostgreSQL.currency')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('currency', 'date')},
            },
        ),
    ]
