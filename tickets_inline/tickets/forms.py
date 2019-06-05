from django import forms

from .models import *

class ReservationForm(forms.ModelForm):
    b_day = forms.DateField(input_formats=['%d%b%y'])

    class Meta:
        model = Reservation
        fields = ('user.name', 'user.last_name', 'user.phone_number', 'user.email')