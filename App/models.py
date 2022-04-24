from django.db import models
from datetime import datetime 
from django.db.models.signals import pre_save

# Create your models here.
class Rental(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name 

class Reservation(models.Model):
    created_at = models.DateTimeField(default=datetime.utcnow, null=True, blank=True)
    rental_id = models.ForeignKey(Rental, on_delete = models.CASCADE)
    reservation_id = models.CharField(max_length=200)
    checkin = models.DateField()
    checkout = models.DateField()
    previous_reservation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.reservation_id

def pre_save_previous_reservation(instance, sender, *args, **kwargs):
    if instance.reservation_id == Reservation.objects.filter(rental_id=instance.rental_id).last():
        instance.previous_reservation = None
    else:
        if instance.pk:
            pass 
        else:
            instance.previous_reservation= str(Reservation.objects.filter(rental_id=instance.rental_id).last())



    
    
pre_save.connect(pre_save_previous_reservation, sender= Reservation)

    