# Generated by Django 3.2.11 on 2022-02-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taschengeldapp', '0007_alter_buchung_options_alter_konto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buchung',
            name='beschreibung',
            field=models.CharField(default='', max_length=200),
        ),
    ]