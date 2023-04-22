from django.db import models

class System1_Temperature(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class System1_Humidity(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class System1_Occupancy(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    
class System2_Ph(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class System2_Turbidity(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class System2_Conductivity(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class System3_Water_Level(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class System3_Pressure(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class System3_Temperature(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
