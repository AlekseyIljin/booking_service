import django.forms as forms
from .models import AIRPORTS
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
    widgets = forms.DateField(widget=forms.TextInput(attrs={
        'class':'datapicker'
    }))
