from django.db import models

class BikeType(models.Model):
    name = models.CharField(max_length=50)

class BikeModelBike(models.Model):
    name = models.CharField(max_length=100)
    typeId = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description = models.TextField(blank=True, null=True)
    typeColor = models.CharField(max_length=50, blank=True, null=True)
    components = models.ManyToManyField('ComponentsApp.BikeModelComponent', through='BikesApp.BikeConfigurationPerBike')

class BikeConfigurationPerBike(models.Model):
    bike = models.ForeignKey("BikesApp.BikeModelBike", on_delete=models.CASCADE)
    component = models.ForeignKey("ComponentsApp.BikeModelComponent", on_delete=models.CASCADE)

