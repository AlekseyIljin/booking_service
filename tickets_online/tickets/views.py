from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import FormView
from .models import Flight, Company, Reservation
from .forms import ReservationForm, FlightList, CustomerCreationForm
from .controllers import FlightController, CustomerController


def index(request):
    airlines = Company.objects.order_by('name')
    return render(request, 'tickets/index.html', {'airlines': airlines})


class FlightViews(View):
    model = Flight
    template = 'tickets/flights.html'

    def get(self, request, *args, **kwargs):
        flights = self.model.objects.order_by('flight_number')
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
        for reservation in reservations:
            reservation.cost = reservation.fare.cost + reservation.flight.tax
        return render(request, self.template,
                      {'pnrs': reservations})


class ReservationCreateView(View):
    model = Reservation
    form_class = ReservationForm
    initial = {"key": 'value'}
    template_name = 'tickets/create_booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,
                      {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            controller = FlightController()
            resulted_data = controller.choices_of_flights(data.get('departure'), data.get('destination'),
                                                          data.get('date'))
            request.session['flight_selection'] = resulted_data
            return HttpResponseRedirect('flight_selection')


class SelectFlightFromListView(FormView):
    initial = {"key": 'value'}
    model = Reservation
    form_class = FlightList
    template_name = 'tickets/create_booking.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['flight_number'] = self.request.session.get('flight_selection')

        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            controller = CustomerController
            resulted_data = controller.create_customer()
            request.session['flight_selection'] = resulted_data
            return HttpResponseRedirect('flight_selection')


class CustomerInputView(FormView):
    initial = {"key": 'value'}
    model = Reservation
    form_class = CustomerCreationForm
    template_name = 'tickets/create_booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,
                      {'customer': form})
