byte val=0;
int val_x=0;
int val_y=0;
int val_z=0;
int val_max=5096;
int val_min=-5096;
int stp_l=256;
int stp_ls=48;
int stp_s=16;
int stp_ss=8;

//#define LED_PIN 13
#include <Stepper.h>

const int MOTOR_STEPS = 2048;
//step number/turn and pin No.
Stepper myStepper_x(MOTOR_STEPS,13,11,12,10);
Stepper myStepper_y(MOTOR_STEPS,9,7,8,6);
Stepper myStepper_z(MOTOR_STEPS,5,3,4,2);

void setup(){
  //pinMode(LED_PIN, OUTPUT);
  myStepper_x.setSpeed(6);//6turn/min
  myStepper_y.setSpeed(6);
  myStepper_z.setSpeed(6);
  Serial.begin(9600);
}

void loop() {
  val = Serial.read();
  // x axis
  if(val == 'a') {
    if(val_x <= val_max-stp_l) {
      myStepper_x.step(stp_l); //90 deg by 521step;
      val_x=val_x+stp_l;
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
    }
    else if (val_x > val_max-stp_l) {
      myStepper_x.step(val_max-val_x); //90 deg by 521step;
      val_x=val_max;
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
    }
  }
  else if (val == 'b') {
    if(val_x <= val_max-stp_s) {
      myStepper_x.step(stp_s); //90 deg by 521step;
      val_x=val_x+stp_s;
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
    }
    else if (val_x > val_max-stp_s) {
      myStepper_x.step(val_max-val_x); //90 deg by 521step;
      val_x=val_max;
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
    }
  }
  else if (val == 'c') {
    myStepper_x.step(-val_x); //90 deg by 521step;
    val_x=0;
    digitalWrite(10,LOW);
    digitalWrite(11,LOW);
    digitalWrite(12,LOW);
    digitalWrite(13,LOW);
  }
  else if (val == 'd') {
    if(val_x >= val_min+stp_s) {
      myStepper_x.step(-stp_s); //90 deg by 521step;
      val_x=val_x-stp_s;
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
    }
    else if (val_x < val_min+stp_s) {
      myStepper_x.step(val_min-val_x); //90 deg by 521step;
      val_x=val_min;
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
    }
  }
  else if (val == 'e') {
   if(val_x >= val_min+stp_l) {
      myStepper_x.step(-stp_l); //90 deg by 521step;
      val_x=val_x-stp_l;
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
    }
    else if (val_x < val_min+stp_l) {
      myStepper_x.step(val_min-val_x); //90 deg by 521step;
      val_x=val_min;
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
    }
  }
  
  // y axis
  else if (val == 'f') {
    if(val_y <= val_max-stp_l) {
      myStepper_y.step(stp_l); //90 deg by 521step;
      val_y=val_y+stp_l;
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
    else if (val_y > val_max-stp_l) {
      myStepper_y.step(val_max-val_y); //90 deg by 521step;
      val_y=val_max;
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
  }
  else if (val == 'g') {
    if(val_y <= val_max-stp_s) {
      myStepper_y.step(stp_s); //90 deg by 521step;
      val_y=val_y+stp_s;
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
    else if (val_y > val_max-stp_s) {
      myStepper_y.step(val_max-val_y); //90 deg by 521step;
      val_y=val_max;
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
  }
  else if (val == 'h') {
    myStepper_y.step(-val_y); //90 deg by 521step;
    val_y=0;
    digitalWrite(6,LOW);
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
    digitalWrite(9,LOW);
  }
  else if (val == 'i') {
    if(val_y >= val_min+stp_s) {
      myStepper_y.step(-stp_s); //90 deg by 521step;
      val_y=val_y-stp_s;
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
    else if (val_y < val_min+stp_s) {
      myStepper_y.step(val_min-val_y); //90 deg by 521step;
      val_y=val_min;
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
  }
  else if (val == 'j') {
    if(val_y >= val_min+stp_l) {
      myStepper_y.step(-stp_l); //90 deg by 521step;
      val_y=val_y-stp_l;
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
    else if (val_y < val_min+stp_l) {
      myStepper_y.step(val_min-val_y); //90 deg by 521step;
      val_y=val_min;
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
  }
  
  //z axis
  else if (val == 'k') {
    if(val_z <= val_max-stp_l) {
      myStepper_z.step(stp_l); //90 deg by 521step;
      val_z=val_z+stp_l;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
    else if (val_z > val_max-stp_l) {
      myStepper_z.step(val_max-val_z); //90 deg by 521step;
      val_z=val_max;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
  }
  else if (val == 'l') {
    if(val_y <= val_max-stp_s) {
      myStepper_z.step(stp_s); //90 deg by 521step;
      val_z=val_z+stp_s;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
    else if (val_z > val_max-stp_s) {
      myStepper_z.step(val_max-val_z); //90 deg by 521step;
      val_z=val_max;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
  }
  else if (val == 'm') {
    myStepper_z.step(-val_z); //90 deg by 521step;
    val_z=0;
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
    digitalWrite(5,LOW);
  }
  else if (val == 'n') {
    if(val_z >= val_min+stp_s) {
      myStepper_z.step(-stp_s); //90 deg by 521step;
      val_z=val_z-stp_s;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
    else if (val_z < val_min+stp_s) {
      myStepper_z.step(val_min-val_z); //90 deg by 521step;
      val_z=val_min;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
  }
  else if (val == 'o') {
    if(val_z >= val_min+stp_l) {
      myStepper_z.step(-stp_l); //90 deg by 521step;
      val_z=val_z-stp_l;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
    else if (val_z < val_min+stp_l) {
      myStepper_z.step(val_min-val_z); //90 deg by 521step;
      val_z=val_min;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
  }
  else if (val == 'q') {
    if(val_y <= val_max-stp_ls) {
      myStepper_z.step(stp_ls); //90 deg by 521step;
      val_z=val_z+stp_ls;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
    else if (val_z > val_max-stp_ls) {
      myStepper_z.step(val_max-val_z); //90 deg by 521step;
      val_z=val_max;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
  }
  else if (val == 'r') {
    if(val_y <= val_max-stp_ss) {
      myStepper_z.step(stp_ss); //90 deg by 521step;
      val_z=val_z+stp_ss;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
    else if (val_z > val_max-stp_ss) {
      myStepper_z.step(val_max-val_z); //90 deg by 521step;
      val_z=val_max;
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
    }
  }
  else if (val == 'p') {
    myStepper_x.step(-val_x); //90 deg by 521step;
    myStepper_y.step(-val_y); //90 deg by 521step;
    myStepper_z.step(-val_z); //90 deg by 521step;
    val_x=0;
    val_y=0;
    val_z=0;
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
    digitalWrite(5,LOW);
    digitalWrite(6,LOW);
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
    digitalWrite(9,LOW);
    digitalWrite(10,LOW);
    digitalWrite(11,LOW);
    digitalWrite(12,LOW);
    digitalWrite(13,LOW);
  }
}

//void loop() {
//  if(Serial.available() > 0 ) {
//      val = Serial.read();
//  }
//  if(val == '1') digitalWrite(LED_PIN,HIGH);
//  else if (val == '2') digitalWrite(LED_PIN,LOW);
//  else if (val == '3') digitalWrite(LED_PIN,HIGH);
//  else if (val == '4') digitalWrite(LED_PIN,LOW);
//  else if (val == '5') digitalWrite(LED_PIN,HIGH);
//  else if (val == '6') digitalWrite(LED_PIN,LOW);
//  else if (val == '7') digitalWrite(LED_PIN,HIGH);
//  else if (val == '8') digitalWrite(LED_PIN,LOW);
//  else if (val == '9') digitalWrite(LED_PIN,HIGH);
//  else if (val == '10') digitalWrite(LED_PIN,LOW);
//  else if (val == '11') digitalWrite(LED_PIN,HIGH);
//  else if (val == '12') digitalWrite(LED_PIN,LOW);
//  else if (val == '13') digitalWrite(LED_PIN,HIGH);
//  else if (val == '14') digitalWrite(LED_PIN,LOW);
//  else if (val == '15') digitalWrite(LED_PIN,HIGH);
//  else if (val == '16') digitalWrite(LED_PIN,LOW);
//}

