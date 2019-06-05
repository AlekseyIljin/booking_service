# Generated by Django 2.2.1 on 2019-06-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20190604_1451'),
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
            field=models.CharField(choices=[('IEV', 'Жуляны'), ('ODS', 'Одесса'), ('KHE', 'Херсон'), ('AMS', 'Амстердам'), ('IST', 'Стамбул'), ('BCN', 'Барселона'), ('OZH', 'Запорожье'), ('CWC', 'Черновцы'), ('LWO', 'Львов'), ('PRG', 'Прага'), ('VIN', 'Винница'), ('KBP', 'Борисполь'), ('DNK', 'Днепр'), ('HRK', 'Харьков')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(choices=[('IEV', 'Жуляны'), ('ODS', 'Одесса'), ('KHE', 'Херсон'), ('AMS', 'Амстердам'), ('IST', 'Стамбул'), ('BCN', 'Барселона'), ('OZH', 'Запорожье'), ('CWC', 'Черновцы'), ('LWO', 'Львов'), ('PRG', 'Прага'), ('VIN', 'Винница'), ('KBP', 'Борисполь'), ('DNK', 'Днепр'), ('HRK', 'Харьков')], max_length=3, null=True),
        ),
    ]
