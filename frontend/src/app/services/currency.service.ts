import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { CurrencyRate } from './currency.interface';

@Injectable({
  providedIn: 'root',
})
export class CurrencyService {
  private apiBaseUrl = 'http://127.0.0.1:8080';

  constructor(private http: HttpClient) {}

  getCurrentRates(): Observable<CurrencyRate[]> {
    const currentDate = new Date();

    if (this.isWeekend(currentDate.toString())) {
      return of([]);
    }

    return this.http.get<CurrencyRate[]>(this.apiBaseUrl + '/current');
  }

  getSpecyficDateRates(date: string): Observable<CurrencyRate[]> {
    if (this.isWeekend(date)) return of([]);

    return this.http.get<CurrencyRate[]>(this.apiBaseUrl + '/rates/' + date);
  }

  getDateRangeRates(
    startDate: string,
    endDate: string
  ): Observable<CurrencyRate[]> {
    return this.http.get<CurrencyRate[]>(
      this.apiBaseUrl + '/rates/' + startDate + '/' + endDate
    );
  }

  private isWeekend(date: string): boolean {
    const dayOfWeek = new Date(date).getDay();

    return dayOfWeek === 0 || dayOfWeek === 6;
  }
}
