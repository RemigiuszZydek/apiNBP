import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CurrencyService } from '../../services/currency.service';
import { CurrencyRate } from '../../services/currency.interface';

@Component({
  selector: 'app-currency',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './currency.component.html',
  styleUrls: ['./currency.component.css'],
})
export class CurrencyComponent {
  currencyRates: CurrencyRate[] = [];
  selectedDate: string = '';
  selectedStartDate: string = '';
  selectedEndDate: string = '';
  isRatesEmpty: boolean = false;

  constructor(private currencyService: CurrencyService) {}

  fetchCurrentRates() {
    this.currencyService
      .getCurrentRates()
      .subscribe((rates: CurrencyRate[]) => {
        this.currencyRates = rates;
        this.isRatesEmpty = rates.length === 0;
      });
  }

  fetchSpecyficDateRates() {
    this.currencyService
      .getSpecyficDateRates(this.selectedDate)
      .subscribe((rates: CurrencyRate[]) => {
        this.currencyRates = rates;
        this.isRatesEmpty = rates.length === 0;
      });
  }

  fetchDateRangeRates() {
    this.currencyService
      .getDateRangeRates(this.selectedStartDate, this.selectedEndDate)
      .subscribe((rates: CurrencyRate[]) => {
        this.currencyRates = rates;
        this.isRatesEmpty = rates.length === 0;
      });
  }
}
