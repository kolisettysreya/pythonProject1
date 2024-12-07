from django.shortcuts import render,redirect

# Create your views here.
def restauranthomepage(request):
    return render(request,'Restaurant/restauranthomepage.html')
def rrdarbar(request):
    return render(request,'Restaurant/rrdarbar.html')
'''def DineIn(request):
    return render(request,'Restaurant/DineIn.html')

from django.shortcuts import render, redirect
from .forms import ReservationForm


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Save the reservation to the database
            form.save()
            # Redirect to a success page
            return render(request, 'Restaurant/reservation_success.html')
    else:
        # Display an empty form for GET requests
        form = ReservationForm()

    # Render the reservation form
    return render(request, 'Restaurant/reservation_form.html', {'form': form})

'''
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import TableBooking
from .forms import TableBookingForm, CancelBookingForm

# Function to check seat availability
def check_availability():
    total_tables = 100
    booked_tables = TableBooking.objects.filter(is_canceled=False).count()
    return total_tables - booked_tables


def book_table(request):
    available_seats = check_availability()
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            if available_seats > 0:
                booking = form.save()  # Save the booking
                # Send confirmation email
                send_mail(
                    subject="Table Reservation Confirmation",
                    message=f"Your table for {booking.guests} guests on {booking.arrival_date} at {booking.arrival_time} is confirmed.\nBooking ID: {booking.id}\nName: {booking.name}",
                    from_email="example@restaurant.com",
                    recipient_list=[booking.email],
                    fail_silently=False,
                )
                return render(request, 'Restaurant/reservation_success.html', {'booking': booking, 'available_seats': check_availability()})
            else:
                return HttpResponse("Sorry, no tables are available.")
    else:
        form = TableBookingForm()

    return render(request, 'Restaurant/DineIn.html', {'form': form, 'available_seats': available_seats})

# Function to handle table booking cancellation
def cancel_booking(request):
    if request.method == 'POST':
        form = CancelBookingForm(request.POST)
        if form.is_valid():
            booking_id = form.cleaned_data['booking_id']
            try:
                booking = TableBooking.objects.get(id=booking_id)
                if booking.is_canceled:
                    return HttpResponse(f"Booking ID {booking_id} has already been canceled.")

                # Remove the booking from the database
                booking.delete()

                return HttpResponse(f"Booking ID {booking_id} has been successfully canceled.")
            except TableBooking.DoesNotExist:
                return HttpResponse("No booking found with the provided Booking ID.")
    else:
        form = CancelBookingForm()

    return render(request, 'Restaurant/cancel_booking.html', {'form': form, 'available_seats': check_availability()})