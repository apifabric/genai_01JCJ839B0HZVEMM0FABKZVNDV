import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './ReservationService-card.component.html',
  styleUrls: ['./ReservationService-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.ReservationService-card]': 'true'
  }
})

export class ReservationServiceCardComponent {


}