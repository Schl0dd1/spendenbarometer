# Generated by Django 3.2.11 on 2022-01-05 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taschengeldapp', '0003_auto_20220105_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buchung',
            name='betrag',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='konto',
            name='aktueller_kontostand',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
