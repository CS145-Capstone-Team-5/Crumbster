#include <Arduino.h>
#include "HX711.h"

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

HX711 scale;

void setup() {
  Serial.begin(57600);

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(-409.42);
  scale.tare();               
      
  Serial.println("LOAD SENSOR READINGS");
}

void loop() {
  Serial.print("Weight:\t");
  Serial.print(scale.get_units(5),0);
  Serial.println(" g");
 
  delay(5000);
}
