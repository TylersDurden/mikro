/** Arduino Light Experiments **/

const int analog1 = A0;       //Vx of joystick
const int analog2 = A2;       //Vy of joystick
const int analog3 = A3;       //SW(Button) on joystick

const int ledR = 10;              //D9
const int ledY = 12;            //D10
const int ledG = 13;            //D11
const int ledB = 11;            //D12

int sense1 = 0;                   // Vx Analog Counter
int sense2 = 0;                   // Vy Analog Counter
int sense3 = 0;                   // Sw Analog Counter
int sum = 0;

bool bounced = false;

void setup() {
  // Start up serial communication for debugging
  Serial.begin(9600);
  // prep the digital outputs
  pinMode(ledR, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
  
}

void loop() {
  // Create a bouncing signal (triangle wave) that oscillates b/w 0-450
  if(sum < 500 & !bounced) sum ++;
  if(bounced) sum-- ;
  if(sum >=450){ bounced = true;}
  if(sum==0){ bounced = false;}
  
  if(sum < 100){
    digitalWrite(ledR, HIGH);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, LOW);
    digitalWrite(ledB, LOW);
  }

  if(sum > 100 && sum < 200){
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, HIGH);
    digitalWrite(ledG, LOW);
    digitalWrite(ledB, LOW);
  }

  if(sum > 200 && sum < 300){
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, HIGH);
    digitalWrite(ledB, LOW);
  }

  if(sum > 400){
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, LOW);
    digitalWrite(ledB, HIGH);
  }
 
  
  // Serial.println(sum);
  // Sleep for 3ms to let A/D settle
  delay(1);
}
