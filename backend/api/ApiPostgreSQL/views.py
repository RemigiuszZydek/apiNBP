from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Currency, ExchangeRate
from datetime import datetime
import requests

def is_weekday(date):
    return date.weekday() < 5

def get_specific_date_currency_rates_from_nbp(date):
    response = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/A/{date}?format=json')
    data = response.json()

    for item in data[0]['rates']:
        currency, _ = Currency.objects.get_or_create(
            code=item['code'],
            defaults={'name': item['currency']}
        )

        ExchangeRate.objects.create(
            currency=currency,
            rate=item['mid'],
            date=date
        )

def get_specific_date_range_currency_rates_from_nbp(start_date, end_date):
    response = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/A/{start_date}/{end_date}?format=json')
    data = response.json()

    for table in data:
        rates_date = datetime.strptime(table['effectiveDate'], '%Y-%m-%d').date()
        if not ExchangeRate.objects.filter(date=rates_date).exists():
            for item in table['rates']:
                currency, _ = Currency.objects.get_or_create(
                    code=item['code'],
                    defaults={'name': item['currency']}
                )

                ExchangeRate.objects.create(
                    currency=currency,
                    rate=item['mid'],
                    date=rates_date
                )

class CurrentCurrencyRatesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        current_date = datetime.now().date()

        if is_weekday(current_date):
            if not ExchangeRate.objects.filter(date=current_date).exists():
                get_specific_date_currency_rates_from_nbp(current_date)

        rates = ExchangeRate.objects.filter(date=current_date)
        serialized_data = [{'currency': rate.currency.name, 'rate': rate.rate, 'date': rate.date} for rate in rates]

        return Response(serialized_data)

class SpecificDateCurrencyRatesAPIView(APIView):
    def get(self, request, date, *args, **kwargs):
        date = datetime.strptime(date, '%Y-%m-%d').date()

        if is_weekday(date):
            if not ExchangeRate.objects.filter(date=date).exists():
                get_specific_date_currency_rates_from_nbp(date)

        rates = ExchangeRate.objects.filter(date=date)
        serialized_data = [{'currency': rate.currency.name, 'rate': rate.rate, 'date': rate.date} for rate in rates]

        return Response(serialized_data)

class DateRangeCurrencyRatesAPIView(APIView):
    def get(self, request, start_date, end_date, *args, **kwargs):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        get_specific_date_range_currency_rates_from_nbp(start_date, end_date)

        rates = ExchangeRate.objects.filter(date__range=[start_date, end_date])
        serialized_data = [{'currency': rate.currency.name, 'rate': rate.rate, 'date': rate.date} for rate in rates]
        sorted_data = sorted(serialized_data, key=lambda x: x['date'])

        return Response(sorted_data)