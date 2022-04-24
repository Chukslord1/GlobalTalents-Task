from django.test import TestCase
from . models import Rental, Reservation, pre_save_previous_reservation
import datetime 
from django.urls import reverse
# Create your tests here.
class ReservationTestCase(TestCase):
    def setUp(self):
        Rental.objects.create(name="rental-2")
        rental = Rental.objects.get(name="rental-2")
        new_reservation = Reservation.objects.create(rental_id=rental, reservation_id="RES-6", checkin=datetime.date(2022, 1,1), checkout=datetime.date(2022, 1, 13))
        new_reservation.save()


    def test_previous_reservation(self):
        """Check if the previous reservation was set"""
        reservation = Reservation.objects.get(reservation_id="RES-6")
        self.assertEqual(reservation.previous_reservation, "RES-6")

class ViewTest(TestCase):

    def test_view_returns_OK(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('App:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')