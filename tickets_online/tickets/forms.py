import django.forms as forms
from .models import AIRPORTS


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
    date = forms.DateField(widget=forms.SelectDateWidget())


class FlightList(forms.Form):

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('flight_number')
        super(FlightList, self).__init__(*args, **kwargs)
        self.fields['flight_number'].choices = choices

    flight_number = forms.ChoiceField(label="Информация о рейсе",
                                      initial='',
                                      widget=forms.Select(),
                                      required=True)


class CustomerCreationForm(forms.Form):
    last_name = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput())
    name = forms.CharField(label='Имя', required=True)
    passport = forms.CharField(label='Серия и номер паспорта', required=True)
    phone = forms.IntegerField(label='Введите номер телефона', required=True)
    email = forms.EmailField(label='Введите адрес электронной почты', required=True)
