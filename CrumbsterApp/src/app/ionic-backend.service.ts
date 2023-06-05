import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, of, pipe } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

export interface Data {
  fact: string;
  tip: string;
  dataLog: string;
}

@Injectable({
  providedIn: 'root'
})
export class IonicBackendService {
  // URL is the IP address. Change this when needed and always retain :5000 (end)
  private url: string = 'IP ADDRESS'
  constructor(private http: HttpClient) { }

  getApi(): Observable<Data> {
    return this.http.get<Data>(this.url)
  }
}
