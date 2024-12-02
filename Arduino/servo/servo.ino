#include <Servo.h>
Servo servo;
int tiltball = 1;
void setup()
{
  servo.attach(10);
  pinMode(tiltball, INPUT);
}

void loop() 
{
  if (analogRead(tiltball) > 30)
  {
    servo.write(90);
  }
  else
  {
    servo.write(0);
  }
  delay(250);
}
