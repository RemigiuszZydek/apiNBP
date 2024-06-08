from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from datetime import datetime

class CurrencyRatesAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_current_currency_rates(self):
        url = reverse('current-currency-rates')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertIn('currency', response.data[0])
        # self.assertIn('rate', response.data[0])
        # self.assertIn('date', response.data[0])

 


def test_specific_date_currency_rates(self):
    date = '2021-11-10'
    response = self.client.get('/api/currency_rates/', {'date': date})
    expected_date = datetime.strptime(date, '%Y-%m-%d').date()
    self.assertEqual(datetime.strptime(response.data[0]['date'], '%Y-%m-%d').date(), expected_date)




def test_date_range_currency_rates(self):
    response = self.client.get('/api/currency_rates/', {'start_date': '2021-01-01', 'end_date': '2021-12-31'})
    start_date = datetime.strptime('2021-01-01', '%Y-%m-%d').date()
    end_date = datetime.strptime('2021-12-31', '%Y-%m-%d').date()
    self.assertTrue(all(start_date <= datetime.strptime(item['date'], '%Y-%m-%d').date() <= end_date for item in response.data))