import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.crumbster.app',
  appName: 'Crumbster',
  webDir: 'www',
  server: {
    androidScheme: 'http', // Android would use http instead of https
    'cleartext': true      // Allows us to to use http urls
  },
  plugins: {
    PushNotifications: {
      presentationOptions: ["badge", "sound", "alert"]
    }
  }
};

export default config;
