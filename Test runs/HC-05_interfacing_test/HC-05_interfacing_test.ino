#include<SoftwareSerial.h>

//Creating an object of SoftwareSerial class named as bt
SoftwareSerial bt(2,3); //(Rx,TX)


void setup() {
  bt.begin(9600);
  Serial.begin(9600);
}

void loop() {
  if(bt.available())
  {
    Serial.write(bt.read()); //Printing the characters received on the serial monitor. 
  }
}
