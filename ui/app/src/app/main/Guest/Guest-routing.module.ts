import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GuestHomeComponent } from './home/Guest-home.component';
import { GuestNewComponent } from './new/Guest-new.component';
import { GuestDetailComponent } from './detail/Guest-detail.component';

const routes: Routes = [
  {path: '', component: GuestHomeComponent},
  { path: 'new', component: GuestNewComponent },
  { path: ':id', component: GuestDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Guest-detail-permissions'
      }
    }
  },{
    path: ':guest_id/Reservation', loadChildren: () => import('../Reservation/Reservation.module').then(m => m.ReservationModule),
    data: {
        oPermission: {
            permissionId: 'Reservation-detail-permissions'
        }
    }
}
];

export const GUEST_MODULE_DECLARATIONS = [
    GuestHomeComponent,
    GuestNewComponent,
    GuestDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class GuestRoutingModule { }