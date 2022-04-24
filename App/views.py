from django.shortcuts import render
from . models import Rental, Reservation
# Create your views here.
def index(request):
    all_reservations = Reservation.objects.all()
    context = {"reservations":all_reservations}
    return render(request, "index.html", context) 
