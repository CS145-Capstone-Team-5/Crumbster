import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, of, pipe } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
export interface Data {
  fact: string;
  tip: string;
}

@Injectable({
  providedIn: 'root'
})
export class IonicBackendService {
  public pressedOnce: number = 0;
  private url: string = 'http://192.168.173.157:5000/'
  constructor(private http: HttpClient) { }

  getApi(): Observable<Data> {
    return this.http.get<Data>(this.url)
  }
}
