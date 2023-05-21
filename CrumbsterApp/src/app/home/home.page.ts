import { Component } from '@angular/core';
import { Data, IonicBackendService } from '../ionic-backend.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  public obtainedData!: Data;

  constructor(private _api: IonicBackendService, private _buttonPressedOnce: IonicBackendService) { }

  callGetApi() {
    this._api.getApi()
      .subscribe(data => this.obtainedData = data);
    if (this.obtainedData === null || this.obtainedData === undefined) {

    }
  }
}
