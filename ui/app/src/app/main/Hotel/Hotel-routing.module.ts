import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HotelHomeComponent } from './home/Hotel-home.component';
import { HotelNewComponent } from './new/Hotel-new.component';
import { HotelDetailComponent } from './detail/Hotel-detail.component';

const routes: Routes = [
  {path: '', component: HotelHomeComponent},
  { path: 'new', component: HotelNewComponent },
  { path: ':id', component: HotelDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Hotel-detail-permissions'
      }
    }
  },{
    path: ':hotel_id/Employee', loadChildren: () => import('../Employee/Employee.module').then(m => m.EmployeeModule),
    data: {
        oPermission: {
            permissionId: 'Employee-detail-permissions'
        }
    }
},{
    path: ':hotel_id/Room', loadChildren: () => import('../Room/Room.module').then(m => m.RoomModule),
    data: {
        oPermission: {
            permissionId: 'Room-detail-permissions'
        }
    }
}
];

export const HOTEL_MODULE_DECLARATIONS = [
    HotelHomeComponent,
    HotelNewComponent,
    HotelDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HotelRoutingModule { }