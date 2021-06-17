from django.db import models

# Create your models here.


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.status


class Airplane(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    range = models.IntegerField()
    engines = models.IntegerField()
    capacity = models.IntegerField()

    # a status (ACTIVE, NEW, RETIRED, BROKEN) can be associated with many airplanes
    # a airplane can only have one status
    # Status -- >> Airplane
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
    )

    last_updated = models.TimeField(auto_now_add=True)
     
    def __str__(self) -> str:
        return self.model
