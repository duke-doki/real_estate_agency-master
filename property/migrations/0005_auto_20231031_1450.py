# Generated by Django 2.2.24 on 2023-10-31 11:50

from django.db import migrations


def fill_empty_boxes(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)





class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20231031_1134'),
    ]

    operations = [
        migrations.RunPython(fill_empty_boxes)
    ]
