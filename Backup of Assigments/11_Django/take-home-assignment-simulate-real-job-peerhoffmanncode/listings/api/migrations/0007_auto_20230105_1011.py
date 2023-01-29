# Generated by Django 3.2.16 on 2023-01-05 10:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20230104_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(max_length=10, null=True)),
                ('bathrooms', models.FloatField(default=0.0, null=True)),
                ('bedrooms', models.IntegerField(default=0, null=True)),
                ('home_size', models.CharField(max_length=50, null=True)),
                ('home_type', models.CharField(blank=True, max_length=50, null=True)),
                ('last_sold_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_sold_price', models.IntegerField(blank=True, default=0, null=True)),
                ('link', models.URLField(null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('property_size', models.IntegerField(default=0, null=True)),
                ('rent_price', models.IntegerField(blank=True, null=True)),
                ('rentzestimate_amount', models.IntegerField(default=0, null=True)),
                ('rentzestimate_last_updated', models.DateField(default=django.utils.timezone.now, null=True)),
                ('tax_value', models.FloatField(default=0.0, null=True)),
                ('tax_year', models.IntegerField(default=0, null=True)),
                ('year_built', models.IntegerField(default=0, null=True)),
                ('zestimate_amount', models.IntegerField(default=0, null=True)),
                ('zestimate_last_updated', models.DateField(default=django.utils.timezone.now, null=True)),
                ('zillow_id', models.IntegerField(default=0, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=3, null=True)),
                ('zipcode', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Houses',
        ),
        migrations.AddField(
            model_name='house',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='api.location'),
        ),
    ]