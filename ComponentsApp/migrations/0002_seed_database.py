from django.db import migrations

def seed_BikeComponents(apps, schema_editor):
    BikeModelComponent = apps.get_model("ComponentsApp", "BikeModelComponent")
    db = schema_editor.connection.alias
    BikeModelComponent.objects.using(db).bulk_create([
        BikeModelComponent(name="Front Wheel", description="The front wheel of the bike", category="Wheels", price=50.00),
        BikeModelComponent(name="Rear Wheel", description="The rear wheel of the bike", category="Wheels", price=60.00),
        BikeModelComponent(name="Handlebar", description="The handlebar of the bike", category="Body", price=25.00),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('ComponentsApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_BikeComponents),
    ]
