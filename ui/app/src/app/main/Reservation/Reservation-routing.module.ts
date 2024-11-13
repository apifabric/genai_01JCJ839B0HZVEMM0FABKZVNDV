import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ReservationHomeComponent } from './home/Reservation-home.component';
import { ReservationNewComponent } from './new/Reservation-new.component';
import { ReservationDetailComponent } from './detail/Reservation-detail.component';

const routes: Routes = [
  {path: '', component: ReservationHomeComponent},
  { path: 'new', component: ReservationNewComponent },
  { path: ':id', component: ReservationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Reservation-detail-permissions'
      }
    }
  },{
    path: ':reservation_id/Payment', loadChildren: () => import('../Payment/Payment.module').then(m => m.PaymentModule),
    data: {
        oPermission: {
            permissionId: 'Payment-detail-permissions'
        }
    }
},{
    path: ':reservation_id/ReservationService', loadChildren: () => import('../ReservationService/ReservationService.module').then(m => m.ReservationServiceModule),
    data: {
        oPermission: {
            permissionId: 'ReservationService-detail-permissions'
        }
    }
}
];

export const RESERVATION_MODULE_DECLARATIONS = [
    ReservationHomeComponent,
    ReservationNewComponent,
    ReservationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ReservationRoutingModule { }