# Generated by Django 2.2.24 on 2023-11-02 05:23

from django.db import migrations


def bind_with_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(owner=flat.owner,
                                            owners_phonenumber=flat.owners_phonenumber,
                                            owner_pure_phone=flat.owner_pure_phone
                                            )[0]
        owner.owned_by.set([flat])


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0017_merge_20231102_0821'),
    ]

    operations = [
        migrations.RunPython(bind_with_flats)
    ]
