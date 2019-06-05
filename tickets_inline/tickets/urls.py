from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('flights', FlightViews.as_view(), name="flight"),
    path('companies', CompanyViews.as_view(), name="company"),
    path('reservation', ReservationView.as_view(), name="pnr"),
]
