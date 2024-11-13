import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './MaintenanceRequest-card.component.html',
  styleUrls: ['./MaintenanceRequest-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.MaintenanceRequest-card]': 'true'
  }
})

export class MaintenanceRequestCardComponent {


}