from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from .models import Flight, Company, Reservation
from .forms import ReservationForm


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

class ReservationCreateView(View):
    model = Reservation
    form_class = ReservationForm
    initial = {"key":'value'}
    template_name = 'tickets/create_booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,
                      {'form':form})

    def post(self, request, *args, **kwargs):
        departure = request.post.form.departure




# Create your views here.
