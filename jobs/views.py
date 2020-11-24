from django.shortcuts import render, redirect
from .forms import AddBookingForm
from .models import JobBooking
# Create your views here.
def job_list(request):
    booking = JobBooking.objects.all()
    context = {
        'title': 'booking list',
        'booking': booking,
    }
    return render(request, "jobs/booking_list.html", context)
def add_booking(request):
    if request.method == 'POST':
        form = AddBookingForm(
            request.POST or None, 
            request.FILES or None,
            )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('job:list')
    else:
        form = AddBookingForm()
    context = {
        "form": form,
        "title": "book form",
    }
    return render(request, "jobs/job_booking.html", context)