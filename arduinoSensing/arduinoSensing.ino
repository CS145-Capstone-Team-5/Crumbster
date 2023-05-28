#include <SPI.h>
#include <Ethernet.h>
#include <HX711.h>

// Network settings
byte mac[] = {0xAB, 0xCD, 0xEF, 0xAB, 0xCD, 0xEF}; // Sample MAC address of the Ethernet shield
IPAddress serverIP(101, 201, 0, 100); // Sample IP address of the server
int serverPort = 80; // Sample Port number of the server
String serverPath = "/log"; // Server path to handle the POST request

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

HX711 scale;

EthernetClient client;

void setup() {
  Serial.begin(57600);

  Ethernet.begin(mac);

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(-409.42);
  scale.tare();

  Serial.println("LOAD SENSOR READINGS");
}

void loop() {
  float weight = scale.get_units(5);
  Serial.print("Weight:\t");
  Serial.print(weight, 0);
  Serial.println(" g");

  // connected to the server
  if (client.connect(serverIP, serverPort)) {
    // payload to be sent
    String postData = "weight=" + String(weight, 0);
    client.print("POST " + serverPath + " HTTP/1.1\r\n");
    client.print("Host: " + serverIP.toString() + "\r\n");
    client.print("Content-Type: application/x-www-form-urlencoded\r\n");
    client.print("Content-Length: " + String(postData.length()) + "\r\n");
    client.print("\r\n");
    client.print(postData);
    client.println();
    // end connection
    client.stop();
    Serial.println("Data sent to server");
  } else {
    Serial.println("Failed to connect to server");
  }

  delay(5000);
}
