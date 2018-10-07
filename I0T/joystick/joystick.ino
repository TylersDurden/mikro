/** ARDUINO - JOYSTICK  */

const int analog1 = A0; // Vx of joystick
const int analog2 = A1; // Vy of joystick
const int analog3 = A2; // sw on joystick

const int ledLeft = 4; // D3 is Vx, and also Green LED 
const int ledRight = 5; //D5 is Vy, and also Blue LED 
const int ledButt = 6; // D6 is Switch, and Red LED 


int sense1 = 0; // initialize Vx as zero  
int sense2 = 0; // initialize Vy as zero
int sense3 = 0; // initialize Sw at zero

void setup() {
  //Start up the serial comms
  Serial.begin(9600);
  // Set up the digital outputs 
  pinMode(ledLeft, OUTPUT);
  pinMode(ledRight, OUTPUT);
  pinMode(ledButt, OUTPUT);
}

void loop() {
  //Read in analog pins
  sense1 = analogRead(analog1); // Vx
  sense2 = analogRead(analog2); // Vy
  sense3 = analogRead(analog3); // Switch || Button of Joystick

   if(sense3 == 0){
       Serial.println("BUTTON PRESSED");
       digitalWrite(ledButt, LOW);
       digitalWrite(ledRight,LOW);
       digitalWrite(ledLeft, LOW);
   }

   if(sense2==0 && sense3 >200 && sense1 > 500){
       Serial.println("UP");
       digitalWrite(ledRight,HIGH);
       digitalWrite(ledLeft ,HIGH);
       digitalWrite(ledButt, LOW);
   }

   if(sense2==1023){
       Serial.println("DOWN");
       digitalWrite(ledButt, HIGH);
       digitalWrite(ledRight, LOW);
       digitalWrite(ledLeft, LOW);
   }

   if(sense1==0){
       Serial.println("LEFT");
       digitalWrite(ledLeft, HIGH);
       digitalWrite(ledRight, LOW);
       digitalWrite(ledButt, LOW);
   }

   if(sense1==1023){
       Serial.println("RIGHT");
       digitalWrite(ledRight,HIGH); 
       digitalWrite(ledLeft, LOW);
       digitalWrite(ledButt, LOW);
   }

  // wait 2 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
  delay(5);
}
