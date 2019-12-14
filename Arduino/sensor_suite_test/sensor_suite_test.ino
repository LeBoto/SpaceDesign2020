// Author: Alex Stubbles
// Description: This code echos sensor data from an accelerometer, GPS, thermometer and altimeter to the computer
//
// Thermometer/Altimeter: BPM388
// GPS: Ultimate GPS Breakout v3
// Accelerometer: LSM9DS1 9-DOF
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_GPS.h>
#include <Adafruit_Sensor.h>
#include <SoftwareSerial.h>
#include "Adafruit_BMP3XX.h"
// *******************GPS SETUP*******************
// Connect the GPS TX (transmit) pin to Digital 9
// Connect the GPS RX (receive) pin to Digital 10
SoftwareSerial mySerial(10, 9); // You can change the pin numbers to match your wiring
#define PMTK_SET_NMEA_UPDATE_10HZ "$PMTK220,1000*2F"
// turn on GPRMC and GGA
#define PMTK_SET_NMEA_OUTPUT_RMCGGA "$PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*28"
#define PMTK_Q_RELEASE "$PMTK605*31"
// *******************TEMP/ALT SETUP*******************
#define BMP_SCK 18
#define BMP_MISO 19
#define BMP_MOSI 20
#define BMP_CS 21

#define SEALEVELPRESSURE_HPA (1013.25)
//Adafruit_BMP3XX bmp(BMP_CS); // hardware SPI
Adafruit_BMP3XX bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);

void read_temp_alt(){
  if (! bmp.performReading()) {
    Serial.println("Failed to perform reading :(");
  }
  if (Serial.available()) {
    Serial.print(bmp.temperature);
    Serial.print(",");
    Serial.print(bmp.pressure / 100.0);
    Serial.print(",");
    Serial.print(bmp.readAltitude(SEALEVELPRESSURE_HPA));
    Serial.println();
  }
}

void read_gps() {
  if (Serial.available()) {
   char c = Serial.read();
   Serial.write(c);
   mySerial.write(c);
  }
  if (mySerial.available()) {
    char c = mySerial.read();
    Serial.write(c);
  }
}

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("BMP388 test");
  // Start temp/alt
  if (!bmp.begin()) {
    Serial.println("Could not find a valid BMP3 sensor, check wiring!");
    while (1);
  }
  // Set up oversampling and filter initialization
  bmp.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  bmp.setPressureOversampling(BMP3_OVERSAMPLING_4X);
  bmp.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  mySerial.begin(9600);
  delay(2000);
  mySerial.println(PMTK_Q_RELEASE);
  // you can send various commands to get it started
  mySerial.println(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  mySerial.println(PMTK_SET_NMEA_UPDATE_10HZ);
}

void loop() {
  read_gps();
  // Read from temp/alt
  read_temp_alt();
}
