import { Component, OnInit } from '@angular/core';
import { IonicBackendService } from 'src/app/ionic-backend.service';

@Component({
  selector: 'app-report',
  templateUrl: './report.page.html',
  styleUrls: ['./report.page.scss'],
})
export class ReportPage implements OnInit {
  public factsOrTips!: string;
  public weight!: string;

  constructor(private _api: IonicBackendService) { }

  ngOnInit() {
    // Method called to obtain data from the server via HTTP GET
    this._api.getApi()
      .subscribe(data => {
        this.factsOrTips = JSON.stringify(data.fact) || JSON.stringify(data.tip)
        this.factsOrTips = this.factsOrTips.replace(/["]+/g, '');
        this.weight = JSON.stringify(data.dataLog).replace(/["]+/g, '')
      });
    if (this.factsOrTips === null || this.factsOrTips === undefined) {
      this.factsOrTips = ""
    }
    if (this.weight === null || this.weight === undefined) {
      this.weight = ""
    }
  }
}
