/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-ethernet-shield-2
 */

#include <SPI.h>
#include <EthernetENC.h>
#include <HX711.h>

//Arduino Config
byte mac[] = { 0x28, 0xCD, 0xC4, 0x6F, 0x16, 0xBA };
IPAddress ip(192,168,254,120);
IPAddress gateway(192,168,254,254);
IPAddress DNSserver(8,8,8,8);
IPAddress subnet(255,255,255,0);

//Server Config
IPAddress server(192,168,254,100);

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = A4;
const int LOADCELL_SCK_PIN = A5;

HX711 scale;

EthernetClient client;

float weight;

void setup() {
  Serial.begin(9600);
  Ethernet.begin(mac, ip, DNSserver, gateway, subnet);

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(-409.42);

  scale.tare();
  
}

void loop() {
  weight = scale.get_units(5);
  Serial.print("Weight:\t");
  //Serial.print(weight, 0);
  //Serial.print(weight);
  //Serial.println(" g");

  int finalWeight = weight;

  Serial.print(finalWeight);
  Serial.println(" g");

  int contentLength = 8 + String(finalWeight).length();
  if (client.connect(server,5000))
  {    
    client.println("PUT /log HTTP/1.1");
    client.println("Host: 192.168.254.100:5000");
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.println("Content-Length: " + String(contentLength));
    client.println();
    client.print("dataLog=");
    client.println(finalWeight);
  }
  
  delay(3000);
}

