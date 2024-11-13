import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Guest-card.component.html',
  styleUrls: ['./Guest-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Guest-card]': 'true'
  }
})

export class GuestCardComponent {


}