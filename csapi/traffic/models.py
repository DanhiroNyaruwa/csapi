from __future__ import unicode_literals

from django.db import models


class AADF(models.Model):
    AADFYEAR = models.IntegerField()
    CP = models.IntegerField()
    Estimation_method = models.CharField(max_length=9)
    Estimation_method_detailed = models.CharField(max_length=200)
    Region = models.CharField(max_length=50)
    LocalAuthority = models.CharField(max_length=50)
    Road = models.CharField(max_length=10)
    RoadCategory = models.CharField(max_length=2)
    Easting = models.IntegerField()
    Northing = models.IntegerField()
    StartJunction = models.CharField(max_length=150)
    EndJunction = models.CharField(max_length=150)
    LinkLength_km = models.FloatField()
    LinkLength_miles = models.FloatField()
    PedalCycles = models.IntegerField()
    Motorcycles = models.IntegerField()
    CarsTaxis = models.IntegerField()
    BusesCoaches = models.IntegerField()
    LightGoodsVehicles = models.IntegerField()
    V2AxleRigidHGV = models.IntegerField()
    V3AxleRigidHGV = models.IntegerField()
    V4or5AxleRigidHGV = models.IntegerField()
    V3or4AxleArticHGV = models.IntegerField()
    V5AxleArticHGV = models.IntegerField()
    V6orMoreAxleArticHGV = models.IntegerField()
    AllHGVs = models.IntegerField()
    AllMotorVehicles = models.IntegerField()

    def __str__(self):
        return str(self.CP)
