import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Room-card.component.html',
  styleUrls: ['./Room-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Room-card]': 'true'
  }
})

export class RoomCardComponent {


}