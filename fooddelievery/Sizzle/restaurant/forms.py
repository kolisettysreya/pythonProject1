from django import forms
from .models import TableBooking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['name','guests', 'arrival_time', 'arrival_date', 'specifications', 'email', 'phone_number']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'arrival_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'name': 'name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'guests': 'Number of Guests',
            'arrival_time': 'Time of Arrival',
            'arrival_date': 'Date of Arrival',
            'specifications': 'Special Specifications',

        }




class CancelBookingForm(forms.Form):
    booking_id = forms.IntegerField(
        label="Booking ID",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Booking ID'}),
        help_text="Enter the booking ID of the reservation you want to cancel."
    )

    def clean_booking_id(self):
        # Custom validation to check if the booking_id exists in the database
        booking_id = self.cleaned_data['booking_id']
        try:
            # Check if booking ID exists
            booking = TableBooking.objects.get(id=booking_id)
            if booking.is_canceled:
                raise forms.ValidationError("This booking has already been canceled.")
        except TableBooking.DoesNotExist:
            raise forms.ValidationError("No booking found with this ID.")

        return booking_id