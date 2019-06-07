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
        for i in self.model.objects.filter(departure=departure, destination=destination, date_of_flight=date).values(
                'id', 'flight_number'):
            result.append((i.get('id'), i.get('flight_number')))

        return result
