from django.db import models
from django.contrib.auth.models import User
class TableBooking(models.Model):
    name=models.CharField(max_length=255, default="Default Name")
    guests = models.PositiveIntegerField()
    arrival_time = models.TimeField()
    arrival_date = models.DateField()
    specifications = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)  # New field for email
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # New field for phone number
    is_canceled = models.BooleanField(default=False)
    def str(self):
        return f"Booking for {self.guests} guests on {self.arrival_date} at {self.arrival_time} (Booking ID: {self.id}"