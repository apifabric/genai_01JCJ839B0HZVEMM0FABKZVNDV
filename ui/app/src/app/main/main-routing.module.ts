import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Employee', loadChildren: () => import('./Employee/Employee.module').then(m => m.EmployeeModule) },
    
        { path: 'Guest', loadChildren: () => import('./Guest/Guest.module').then(m => m.GuestModule) },
    
        { path: 'Hotel', loadChildren: () => import('./Hotel/Hotel.module').then(m => m.HotelModule) },
    
        { path: 'MaintenanceRequest', loadChildren: () => import('./MaintenanceRequest/MaintenanceRequest.module').then(m => m.MaintenanceRequestModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'Reservation', loadChildren: () => import('./Reservation/Reservation.module').then(m => m.ReservationModule) },
    
        { path: 'ReservationService', loadChildren: () => import('./ReservationService/ReservationService.module').then(m => m.ReservationServiceModule) },
    
        { path: 'Room', loadChildren: () => import('./Room/Room.module').then(m => m.RoomModule) },
    
        { path: 'Service', loadChildren: () => import('./Service/Service.module').then(m => m.ServiceModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }