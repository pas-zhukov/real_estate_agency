# Generated by Django 2.2.24 on 2023-07-05 07:18

from django.db import migrations
import phonenumbers


def normalize_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        flat.owner_pure_phone = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phones)
    ]