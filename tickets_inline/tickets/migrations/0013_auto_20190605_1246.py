# Generated by Django 2.2.1 on 2019-06-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_auto_20190605_1246'),
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
            field=models.CharField(choices=[('KBP', 'Борисполь'), ('OZH', 'Запорожье'), ('DNK', 'Днепр'), ('LWO', 'Львов'), ('BCN', 'Барселона'), ('IST', 'Стамбул'), ('VIN', 'Винница'), ('HRK', 'Харьков'), ('AMS', 'Амстердам'), ('ODS', 'Одесса'), ('IEV', 'Жуляны'), ('KHE', 'Херсон'), ('CWC', 'Черновцы'), ('PRG', 'Прага')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(choices=[('KBP', 'Борисполь'), ('OZH', 'Запорожье'), ('DNK', 'Днепр'), ('LWO', 'Львов'), ('BCN', 'Барселона'), ('IST', 'Стамбул'), ('VIN', 'Винница'), ('HRK', 'Харьков'), ('AMS', 'Амстердам'), ('ODS', 'Одесса'), ('IEV', 'Жуляны'), ('KHE', 'Херсон'), ('CWC', 'Черновцы'), ('PRG', 'Прага')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='passport',
            name='p_number',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
    ]