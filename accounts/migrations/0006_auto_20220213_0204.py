# Generated by Django 3.0.8 on 2022-02-13 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_willplant'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('kharif_rain', models.FloatField(default=None, blank=True, null=True)),
                ('rabbi_rain', models.FloatField(default=None, blank=True, null=True)),
                ('avg_rain', models.FloatField(default=None, blank=True, null=True)),
                ('kharif_temp', models.FloatField(default=None, blank=True, null=True)),
                ('rabbi_temp', models.FloatField(default=None, blank=True, null=True)),
                ('avg_temp', models.FloatField(default=None, blank=True, null=True)),
                ('ph', models.FloatField(default=None, blank=True, null=True))
            ],
        ),
        migrations.DeleteModel(
            name='approvals',
        ),
        migrations.DeleteModel(
            name='LoanSchemeForFarmers',
        ),
        migrations.DeleteModel(
            name='MarketPrices',
        ),
    ]