import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Hotel-card.component.html',
  styleUrls: ['./Hotel-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Hotel-card]': 'true'
  }
})

export class HotelCardComponent {


}