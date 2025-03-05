#include <Servo.h>

int z = 2;
Servo flaps;
int reading = 0;
int zeroAmount = 0;
bool firstRead = true;

void setup()
{
	pinMode(z, INPUT);
	flaps.attach(1);
	flaps.write(0);
}

void loop()
{
	reading = analogRead(z) - zeroAmount;
	if (firstRead)
	{
		zeroAmount = reading;
		firstRead = false;
	}

	flaps.write(reading);
	delay(15);
}
