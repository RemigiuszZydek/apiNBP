import { TestBed, ComponentFixture } from '@angular/core/testing';
import { CurrencyComponent } from './currency.component';
import { CurrencyService } from '../../services/currency.service';
import {
  HttpClientTestingModule,
  HttpTestingController,
} from '@angular/common/http/testing';
import { FormsModule } from '@angular/forms';
import { CurrencyRate } from '../../services/currency.interface';
import { of } from 'rxjs';

describe('CurrencyComponent', () => {
  let component: CurrencyComponent;
  let fixture: ComponentFixture<CurrencyComponent>;
  let currencyService: jasmine.SpyObj<CurrencyService>;
  let httpTestingController: HttpTestingController;

  beforeEach(async () => {
    const currencyServiceSpy = jasmine.createSpyObj('CurrencyService', [
      'getCurrentRates',
      'getSpecyficDateRates',
      'getDateRangeRates',
    ]);

    await TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, FormsModule, CurrencyComponent], // Importowanie CurrencyComponent zamiast deklaracji
      providers: [{ provide: CurrencyService, useValue: currencyServiceSpy }],
    }).compileComponents();

    fixture = TestBed.createComponent(CurrencyComponent);
    component = fixture.componentInstance;
    currencyService = TestBed.inject(
      CurrencyService
    ) as jasmine.SpyObj<CurrencyService>;
    httpTestingController = TestBed.inject(HttpTestingController);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should fetch current rates', () => {
    const mockRates: CurrencyRate[] = [
      { currency: 'USD', rate: '1.23', date: new Date() },
      { currency: 'EUR', rate: '0.89', date: new Date() },
    ];
    currencyService.getCurrentRates.and.returnValue(of(mockRates));

    component.CurrentCurrency();

    expect(currencyService.getCurrentRates).toHaveBeenCalled();
    expect(component.currencyRates).toEqual(mockRates);
  });

  it('should fetch specific date rates', () => {
    const mockRates: CurrencyRate[] = [
      { currency: 'USD', rate: '1.23', date: new Date() },
      { currency: 'EUR', rate: '0.89', date: new Date() },
    ];
    currencyService.getSpecyficDateRates.and.returnValue(of(mockRates));
    component.selectedDate = '2024-06-11';

    component.DateCurrency();

    expect(currencyService.getSpecyficDateRates).toHaveBeenCalledWith(
      '2024-06-11'
    );
    expect(component.currencyRates).toEqual(mockRates);
  });

  it('should fetch date range rates', () => {
    const mockRates: CurrencyRate[] = [
      { currency: 'USD', rate: '1.23', date: new Date() },
      { currency: 'EUR', rate: '0.89', date: new Date() },
    ];
    currencyService.getDateRangeRates.and.returnValue(of(mockRates));
    component.selectedStartDate = '2024-06-11';
    component.selectedEndDate = '2024-06-12';

    component.DateRangeCurrency();

    expect(currencyService.getDateRangeRates).toHaveBeenCalledWith(
      '2024-06-11',
      '2024-06-12'
    );
    expect(component.currencyRates).toEqual(mockRates);
  });

  it('should set isRatesEmpty to true if no rates are returned', () => {
    currencyService.getCurrentRates.and.returnValue(of([]));

    component.CurrentCurrency();

    expect(currencyService.getCurrentRates).toHaveBeenCalled();
    expect(component.currencyRates).toEqual([]);
    expect(component.isRatesEmpty).toBe(true);
  });
});
