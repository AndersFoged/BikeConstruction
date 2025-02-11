from django.db import migrations

def seed_BikeTypes(apps, schema_editor):
    BikeType = apps.get_model("BikesApp", "BikeType")
    db = schema_editor.connection.alias
    BikeType.objects.using(db).bulk_create([
        BikeType(name="City"),
        BikeType(name="Road"),
        BikeType(name="MTB"),
        BikeType(name="Gravel"),
        BikeType(name="Tandem"),
        BikeType(name="El"),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('BikesApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_BikeTypes),
    ]
