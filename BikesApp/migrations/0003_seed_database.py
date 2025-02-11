from django.db import migrations

def seed_bikes(apps, schema_editor):
    BikeModelBike = apps.get_model("BikesApp", "BikeModelBike")
    db = schema_editor.connection.alias

    # Create bikes first without directly assigning components
    BikeModelBike.objects.using(db).bulk_create([
        BikeModelBike(name="Bike1", typeId=1, price=100, description="Bike1 til 100", typeColor="Blue"),
        BikeModelBike(name="Bike2", typeId=2, price=200, description="Bike2 til 200", typeColor="Red"),
        BikeModelBike(name="Bike3", typeId=3, price=300, description="Bike3 til 300", typeColor="Green"),
    ])

def assign_components(apps, schema_editor):
    """ Assign ManyToMany components separately """
    BikeModelBike = apps.get_model("BikesApp", "BikeModelBike")
    BikeModelComponent = apps.get_model("ComponentsApp", "BikeModelComponent")

    front_wheel = BikeModelComponent.objects.get(name="Front Wheel")
    rear_wheel = BikeModelComponent.objects.get(name="Rear Wheel")
    handlebar = BikeModelComponent.objects.get(name="Handlebar")

    for bike in BikeModelBike.objects.all():
        bike.components.add(front_wheel, rear_wheel, handlebar)


class Migration(migrations.Migration):

    dependencies = [
        ('BikesApp', '0002_seed_database'),
    ]

    operations = [
        migrations.RunPython(seed_bikes),
        migrations.RunPython(assign_components),  # M2M relationships assigned separately
    ]
