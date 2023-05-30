import { Component, OnInit } from '@angular/core';

import {
  ActionPerformed,
  PushNotificationSchema,
  PushNotifications,
  Token,
} from '@capacitor/push-notifications';
import { IonicBackendService } from '../ionic-backend.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})

export class HomePage {
  // App changes depending on the current time of the day
  private date: Date = new Date();
  public currentTime: number = this.date.getHours();
  public cutoffTime: number = 1;
  public visibleAlert: boolean = false;

  public token: string = "";

  addAlert() {
    if (this.visibleAlert === false) {
      this.visibleAlert = true;
    }
  }

  removeAlert() {
    if (this.visibleAlert === true) {
      this.visibleAlert = false;
    }
  }

  constructor() { }

  ngOnInit() {
    console.log('Initializing HomePage');

    // Request permission to use push notifications
    // iOS will prompt user and return if they granted permission or not
    // Android will just grant without prompting
    PushNotifications.requestPermissions().then(result => {
      if (result.receive === 'granted') {
        // Register with Apple / Google to receive push via APNS/FCM
        PushNotifications.register();
      } else {
        // Show some error
      }
    });

    // On success, we should be able to receive notifications
    PushNotifications.addListener('registration',
      (token: Token) => {
        alert('Push registration success, token: ' + token.value);
      }
    );

    // Some issue with our setup and push will not work
    PushNotifications.addListener('registrationError',
      (error: any) => {
        alert('Error on registration: ' + JSON.stringify(error));
      }
    );

    // Show us the notification payload if the app is open on our device
    //PushNotifications.addListener('pushNotificationReceived',
    //  (notification: PushNotificationSchema) => {
    //    alert('Push received: ' + JSON.stringify(notification));
    //  }
    //);

    // Method called when tapping on a notification
    //PushNotifications.addListener('pushNotificationActionPerformed',
    //  (notification: ActionPerformed) => {
    //    alert('Push action performed: ' + JSON.stringify(notification));
    //  }
    //);
  }
}
