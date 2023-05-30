import { Component, OnInit } from '@angular/core';
import { IonicBackendService } from 'src/app/ionic-backend.service';

@Component({
  selector: 'app-report',
  templateUrl: './report.page.html',
  styleUrls: ['./report.page.scss'],
})
export class ReportPage implements OnInit {
  public fact!: string;
  public tip!: string;
  public weight!: string;

  constructor(private _api: IonicBackendService) { }

  ngOnInit() {
    // Method called to obtain data from the server via HTTP GET
    this._api.getApi()
      .subscribe(data => {
        this.fact = JSON.stringify(data.fact).replace(/["]+/g, '')
        this.tip = JSON.stringify(data.tip).replace(/["]+/g, '');
        this.weight = JSON.stringify(data.dataLog).replace(/["]+/g, '');
      });

    // Placed here in case no information could be obtained
    if (this.fact === null || this.fact === undefined) {
      this.fact = ""
    }
    if (this.tip === null || this.tip === undefined) {
      this.tip = ""
    }
    if (this.weight === null || this.weight === undefined) {
      this.weight = ""
    }
  }
}
