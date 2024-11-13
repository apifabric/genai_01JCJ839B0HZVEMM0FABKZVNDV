import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MaintenanceRequestHomeComponent } from './home/MaintenanceRequest-home.component';
import { MaintenanceRequestNewComponent } from './new/MaintenanceRequest-new.component';
import { MaintenanceRequestDetailComponent } from './detail/MaintenanceRequest-detail.component';

const routes: Routes = [
  {path: '', component: MaintenanceRequestHomeComponent},
  { path: 'new', component: MaintenanceRequestNewComponent },
  { path: ':id', component: MaintenanceRequestDetailComponent,
    data: {
      oPermission: {
        permissionId: 'MaintenanceRequest-detail-permissions'
      }
    }
  }
];

export const MAINTENANCEREQUEST_MODULE_DECLARATIONS = [
    MaintenanceRequestHomeComponent,
    MaintenanceRequestNewComponent,
    MaintenanceRequestDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MaintenanceRequestRoutingModule { }