# Generated by Django 2.2.24 on 2023-07-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20230705_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='flats',
        ),
        migrations.AddField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
