# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AirplaneStatus(models.Model):
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'airplane_status'

    def __str__(self) -> str:
        return self.status


class Airplanes(models.Model):
    model = models.CharField(max_length=100)
    range = models.IntegerField()
    engines = models.IntegerField()
    capacity = models.IntegerField()
    status = models.ForeignKey(AirplaneStatus, models.DO_NOTHING, db_column='status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airplanes'

    def __str__(self) -> str:
        return self.model