# Generated by Django 2.2.1 on 2019-06-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0027_auto_20190605_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fare',
            name='service_class',
            field=models.CharField(choices=[('eco', 'economy'), ('bus', 'business'), ('low', 'lowcost')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure',
            field=models.CharField(choices=[('IEV', 'Жуляны'), ('CWC', 'Черновцы'), ('DNK', 'Днепр'), ('ODS', 'Одесса'), ('AMS', 'Амстердам'), ('LWO', 'Львов'), ('PRG', 'Прага'), ('KBP', 'Борисполь'), ('VIN', 'Винница'), ('HRK', 'Харьков'), ('KHE', 'Херсон'), ('IST', 'Стамбул'), ('OZH', 'Запорожье'), ('BCN', 'Барселона')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(choices=[('IEV', 'Жуляны'), ('CWC', 'Черновцы'), ('DNK', 'Днепр'), ('ODS', 'Одесса'), ('AMS', 'Амстердам'), ('LWO', 'Львов'), ('PRG', 'Прага'), ('KBP', 'Борисполь'), ('VIN', 'Винница'), ('HRK', 'Харьков'), ('KHE', 'Херсон'), ('IST', 'Стамбул'), ('OZH', 'Запорожье'), ('BCN', 'Барселона')], max_length=3, null=True),
        ),
    ]
