from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('flights', FlightViews.as_view(), name="flight"),
    path('companies', CompanyViews.as_view(), name="company"),
    path('reservation', ReservationView.as_view(), name="pnr"),
    path('creation', ReservationCreateView.as_view(), name="booking"),
    path('flight_selection', SelectFlightFromListView.as_view(), name="flights"),
    path('customer_input', CustomerInputView.as_view(), name="customer")

]
