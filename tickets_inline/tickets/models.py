from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import re

AIRPORTS = {
    ("ODS", 'Одесса'),
    ("OZH", 'Запорожье'),
    ("KHE", 'Херсон'),
    ("KBP", "Борисполь"),
    ("IEV", 'Жуляны'),
    ("LWO", "Львов"),
    ("CWC", 'Черновцы'),
    ('VIN', "Винница"),
    ('HRK', "Харьков"),
    ('DNK', "Днепр"),
    ('PRG', "Прага"),
    ('AMS', "Амстердам"),
    ('IST', 'Стамбул'),
    ('BCN', 'Барселона'),
}

FARE = {
    ("eco", "economy"),
    ("bus", "business"),
    ("low", "lowcost"),
}


class Company(models.Model):
    name = models.CharField(max_length=250)
    site = models.URLField('site_address')
    loyalty_program = models.BooleanField
    blank = models.IntegerField(max_length=3)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name = "airline"

    def __str__(self):
        return self.name


class Flight(models.Model):
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    flight_number = models.IntegerField(max_length=4)
    departure = models.CharField(null=True, max_length=3, choices=AIRPORTS)
    destination = models.CharField(null=True, max_length=3, choices=AIRPORTS)
    # departure_time = models.DateTimeField()
    # arrival_time = models.DateTimeField()
    tax = models.IntegerField(max_length=10, null=True)


    class Meta:
        verbose_name = "flight"

    def __str__(self):
        return str(self.id_company.code) + str(self.flight_number)


class Fare(models.Model):
    symbol = models.CharField(max_length=1)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service_class = models.CharField(max_length=3, choices=FARE)
    cost = models.FloatField(max_length=5, null=True)

    def __str__(self):
        return str(self.id_company.code) + " - " + str(self.service_class)


class Passport(models.Model):
    citizenship = models.CharField(max_length=3)
    p_number = models.CharField(max_length=250, default='')
    issue = models.CharField(max_length=3)
    b_day = models.DateField (blank=True, null=True)
    sex = models.CharField(max_length=6)
    expity_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.citizenship


class User(models.Model):


    def passport_details(self):
        detail_string = str(Passport.citizenship) + '/' + str(Passport.serial) + str(Passport.number) + '/' + str(
            Passport.issue) + '/'
        + str(Passport.b_day) + str(Passport.sex) + '/' + str(Passport.expity_date)
        return detail_string

    def number_regular(chars):
        phone = re.sub("\d", str(chars))
        return phone

    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE, null=True)
    loyalty = models.BooleanField(default=False)
    phone_number = PhoneNumberField()
    email = models.EmailField(null=True)

    def __str__(self):
        return  self.name + " "+ self.last_name



class Reservation(models.Model):
    pnr = models.CharField(max_length=6, unique=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    fare = models.ForeignKey(Fare, on_delete=models.CASCADE, default=0)
    payment = models.BooleanField(default=False)
    ticket = models.IntegerField(max_length=10, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.pnr + " " + self.user.last_name

# Create your models here.
