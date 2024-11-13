import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {RESERVATIONSERVICE_MODULE_DECLARATIONS, ReservationServiceRoutingModule} from  './ReservationService-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ReservationServiceRoutingModule
  ],
  declarations: RESERVATIONSERVICE_MODULE_DECLARATIONS,
  exports: RESERVATIONSERVICE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ReservationServiceModule { }