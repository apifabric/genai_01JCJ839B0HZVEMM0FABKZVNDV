import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Hotel-new',
  templateUrl: './Hotel-new.component.html',
  styleUrls: ['./Hotel-new.component.scss']
})
export class HotelNewComponent {
  @ViewChild("HotelForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}