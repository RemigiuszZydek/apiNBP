from django.db import models

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True) # kod waluty (USD)
    name = models.CharField(max_length=50) # nazwa waulty (Dolar)

    def __str__(self):
        return f"{self.name} ({self.code})"


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE) #klucz do modelu Currency
    rate = models.DecimalField(max_digits=10, decimal_places=4) # Kurs waluty
    date = models.DateField() # Data kursu

    class Meta:
        unique_together = ('currency', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.currency.code} - {self.rate} on {self.date}"


class ExchangeRateArchive(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE) 
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField()

    class Meta:
        unique_together = ('currency', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"[Archive] {self.currency.code} - {self.rate} on {self.date}" 