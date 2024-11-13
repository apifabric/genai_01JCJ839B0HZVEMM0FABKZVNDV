import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ReservationServiceHomeComponent } from './home/ReservationService-home.component';
import { ReservationServiceNewComponent } from './new/ReservationService-new.component';
import { ReservationServiceDetailComponent } from './detail/ReservationService-detail.component';

const routes: Routes = [
  {path: '', component: ReservationServiceHomeComponent},
  { path: 'new', component: ReservationServiceNewComponent },
  { path: ':id', component: ReservationServiceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ReservationService-detail-permissions'
      }
    }
  }
];

export const RESERVATIONSERVICE_MODULE_DECLARATIONS = [
    ReservationServiceHomeComponent,
    ReservationServiceNewComponent,
    ReservationServiceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ReservationServiceRoutingModule { }