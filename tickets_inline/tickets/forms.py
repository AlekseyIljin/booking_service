import django.forms as forms
from .models import AIRPORTS, Flight
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.Form):
    departure = forms.ChoiceField(label="Отправление",
                                  choices=AIRPORTS,
                                  initial='',
                                  widget=forms.Select(),
                                  required=True)
    destination = forms.ChoiceField(label="Прибытие",
                                    choices=AIRPORTS,
                                    initial='',
                                    widget=forms.Select(),
                                    required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'datapicker'
    }))


class FlightList(forms.Form):
    def __init__(self, choices, **kwargs):
        forms.Form.__init__(self,**kwargs)
        flight_number = forms.ChoiceField(label="Номер рейса",
                                  choices=choices,
                                  initial='',
                                  widget=forms.Select(),
                                  required=True)


