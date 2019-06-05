# Generated by Django 2.2.1 on 2019-06-05 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0017_auto_20190605_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passport',
            name='p_number',
        ),
        migrations.AddField(
            model_name='passport',
            name='number',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='passport',
            name='serial',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='fare',
            name='service_class',
            field=models.CharField(choices=[('bus', 'business'), ('eco', 'economy'), ('low', 'lowcost')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure',
            field=models.CharField(choices=[('KBP', 'Борисполь'), ('PRG', 'Прага'), ('ODS', 'Одесса'), ('DNK', 'Днепр'), ('LWO', 'Львов'), ('HRK', 'Харьков'), ('IST', 'Стамбул'), ('IEV', 'Жуляны'), ('BCN', 'Барселона'), ('KHE', 'Херсон'), ('AMS', 'Амстердам'), ('OZH', 'Запорожье'), ('VIN', 'Винница'), ('CWC', 'Черновцы')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(choices=[('KBP', 'Борисполь'), ('PRG', 'Прага'), ('ODS', 'Одесса'), ('DNK', 'Днепр'), ('LWO', 'Львов'), ('HRK', 'Харьков'), ('IST', 'Стамбул'), ('IEV', 'Жуляны'), ('BCN', 'Барселона'), ('KHE', 'Херсон'), ('AMS', 'Амстердам'), ('OZH', 'Запорожье'), ('VIN', 'Винница'), ('CWC', 'Черновцы')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tickets.User'),
        ),
    ]
