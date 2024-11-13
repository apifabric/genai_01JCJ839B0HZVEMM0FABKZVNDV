import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Reservation-card.component.html',
  styleUrls: ['./Reservation-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Reservation-card]': 'true'
  }
})

export class ReservationCardComponent {


}