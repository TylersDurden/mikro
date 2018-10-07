/**
 * Read out EEPROM to the console
 * Using an Uno, which has 1kb of EEPROM storage. 
 */
#include <EEPROM.h>
// start from first byte of EEPROM
int address = 0;
byte value;

void setup(){
  //start up serial comms
  Serial.begin(9600);
  while (!Serial){
    ;// wait for serial port connection 
  }
  
}

void loop(){
  // Read from EEPROM
  value = EEPROM.read(address);

  Serial.print(address);
  Serial.print("\t");
  Serial.print(value, DEC);
  Serial.println();
  address = address + 1;
  if (address == EEPROM.length()){
    address = 0;
  }
  delay(50);
}
