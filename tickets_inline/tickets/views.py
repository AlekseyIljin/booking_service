from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from .models import Flight, Company, Reservation
# from .forms import ReservationForm


def index(request):
    return render(request, 'tickets/index.html')


class FlightViews(View):
    model = Flight
    template = 'tickets/flights.html'

    def get(self, request, *args, **kwargs):
        flights = self.model.objects.all()[:10]
        return render(request, self.template,
                      {'flights': flights})


class CompanyViews(View):
    model = Company
    template = 'tickets/company.html'

    def get(self, request, *args, **kwargs):
        companies = self.model.objects.all()[:10]
        return render(request, self.template,
                      {'companies': companies})


class ReservationView(View):
    model = Reservation
    template = 'tickets/reservation.html'

    def get(self, request, *args, **kwargs):
        reservations = self.model.objects.all()[:10]
        for i in range(len(reservations)):
            reservations[i].cost = reservations[i].fare.cost + reservations[i].flight.tax
        return render(request, self.template,
                      {'pnrs': reservations})

# class ReservationCreateView(CreateView):
#     template_name = 'tickets/create_booking.html'
#     form_class = ReservationForm
#     success_url = 'tickets/'
# Create your views here.
