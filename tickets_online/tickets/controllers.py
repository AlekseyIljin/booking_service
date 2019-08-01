from .models import Customer, Flight


class CustomerController:
    model = Customer

    def create_customer(self, **kwargs):
        customer = Customer(kwargs=kwargs)
        customer.save()
        return customer.id


class FlightController:
    model = Flight

    def choices_of_flights(self, departure, destination, date):
        result = []
        for i in self.model.objects.filter(departure=departure, destination=destination).values(
                'id', 'id_company__code', 'flight_number', 'departure_time', 'arrival_time'):
            result.append(
                (i.get('id'), f"{i.get('id_company__code')}{i.get('flight_number')}: {i.get('arrival_time')} - "
                              f"{i.get('departure_time')}"))
            return result
