import { Routes } from '@angular/router';
import { CurrencyComponent } from './components/currency/currency.component';

export const routes: Routes = [
  { path: '', redirectTo: 'currency', pathMatch: 'full' },
  { path: 'currency', component: CurrencyComponent },
];
