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
  if(sum<12 && !bounced) sum++;
  if(bounced) sum--;
  if(sum>=12){bounced=true;}
  if(sum==0){bounced=false;}
  
  if(sum == 1){ // 1
    digitalWrite(ledR, HIGH);//1
    digitalWrite(ledY, LOW);//2
    digitalWrite(ledG, LOW);//4
    digitalWrite(ledB, LOW);//8
  }

  if(sum == 2){ //2 
    digitalWrite(ledR, LOW);//1
    digitalWrite(ledY, HIGH);//2
    digitalWrite(ledG, LOW);//4
    digitalWrite(ledB, LOW);//8
  }

  if(sum == 3){ //3
    digitalWrite(ledR, HIGH);//1
    digitalWrite(ledY, HIGH);//2
    digitalWrite(ledG, LOW);//4
    digitalWrite(ledB, LOW);//8
  }

  if(sum == 4){//4
    digitalWrite(ledR, LOW); //1
    digitalWrite(ledY, LOW); //2
    digitalWrite(ledG, HIGH);//4
    digitalWrite(ledB, LOW); //8
  }

  if(sum == 5){//5
    digitalWrite(ledR, HIGH); //1
    digitalWrite(ledY, LOW);  //2
    digitalWrite(ledG, HIGH); //4
    digitalWrite(ledB, LOW);  //8
  }
  if(sum == 6){ //6
    digitalWrite(ledR, LOW);  //1
    digitalWrite(ledY, HIGH); //2
    digitalWrite(ledG, HIGH); //4
    digitalWrite(ledB, LOW);  //8
  }

  if(sum == 7){//7
    digitalWrite(ledR, LOW);   //1
    digitalWrite(ledY, HIGH);  //2
    digitalWrite(ledG, HIGH);  //4
    digitalWrite(ledB, HIGH);  //8
  }
  if(sum == 8){//8
    digitalWrite(ledR, LOW);   //1
    digitalWrite(ledY, LOW);   //2
    digitalWrite(ledG, LOW);   //4
    digitalWrite(ledB, HIGH);  //8
  }
  if(sum == 9){//9
    digitalWrite(ledR, HIGH);  //1
    digitalWrite(ledY, LOW);   //2
    digitalWrite(ledG, LOW);   //4
    digitalWrite(ledB, HIGH);  //8
  }
  if(sum == 10){//10
    digitalWrite(ledR, LOW);   //1
    digitalWrite(ledY, HIGH);  //2
    digitalWrite(ledG, LOW);   //4
    digitalWrite(ledB, HIGH);  //8
  }
  if(sum == 11){//11
    digitalWrite(ledR, HIGH);   //1
    digitalWrite(ledY, HIGH);  //2
    digitalWrite(ledG, LOW);   //4
    digitalWrite(ledB, HIGH);  //8
  }
  if(sum == 12){//12
    digitalWrite(ledR, LOW);   //1
    digitalWrite(ledY, LOW);  //2
    digitalWrite(ledG, HIGH);   //4
    digitalWrite(ledB, HIGH);  //8
  }
  
  // Serial.println(sum);
  // Sleep for 3ms to let A/D settle
  delay(50);
}
