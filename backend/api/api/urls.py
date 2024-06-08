from django.contrib import admin
from django.urls import path
from ApiPostgreSQL.views import CurrentCurrencyRatesAPIView, DateRangeCurrencyRatesAPIView, SpecificDateCurrencyRatesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current/', CurrentCurrencyRatesAPIView.as_view(), name='current-currency-rates'),
    path('rates/<str:date>/', SpecificDateCurrencyRatesAPIView.as_view(), name='specific-date-currency-rates'),
    path('rates/<str:start_date>/<str:end_date>/', DateRangeCurrencyRatesAPIView.as_view(), name='date-range-currency-rates'),
]