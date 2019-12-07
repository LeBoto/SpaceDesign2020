#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

SoftwareSerial my_serial(3, 2); // init serial port
Adafruit_GPS GPS(&my_serial); //Create GPS object

String NMEA1; //frist NMEA
String NMEA2; //second NMEA
char c; //Read char from GPS

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); //serial monitor
  GPS.begin(9600); //Init GPS
  GPS.sendCommand("$PGCMD,33,0*6D"); //Turn off antenna update data
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_10HZ); //Init update of 10 Hz
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA); //Request RMC and GGA
  delay(1000);
}

void loop() {
  read_gps();
}

void read_gps() {
 while(!GPS.newNMEAreceived()){
  c = GPS.read();
  Serial.println(GPS.newNMEAreceived()); //Delete when fixed
 }
 Serial.println("Made it!"); //Delete when fixed
 GPS.parse(GPS.lastNMEA());
 NMEA1 = GPS.lastNMEA();
 while(!GPS.newNMEAreceived()){
  c = GPS.read();
 }
 GPS.parse(GPS.lastNMEA());
 NMEA2 = GPS.lastNMEA();

 Serial.println(NMEA1);
 Serial.println(NMEA2);
 
}
