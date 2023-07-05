# Generated by Django 2.2.24 on 2023-07-05 20:29

from django.db import migrations


def flat_and_owner(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        owners = Owner.objects.filter(
            full_name=flat.owner,
            phonenumber=flat.owners_phonenumber
        )
        flat.owners.set(owners)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230705_2323'),
    ]

    operations = [
        migrations.RunPython(flat_and_owner)
    ]