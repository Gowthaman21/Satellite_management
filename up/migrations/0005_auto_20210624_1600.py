# Generated by Django 2.2.12 on 2021-06-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('up', '0004_auto_20210624_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Expected_lifetime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='GEO_longitude',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='NORAD_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='apogee',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='dry_mass',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='inclination',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='launch_mass',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='perigee',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='period',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='power',
            field=models.CharField(max_length=50),
        ),
    ]