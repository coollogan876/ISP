#include <Wire.h>
#include "MAX30105.h"

MAX30105 sensor;

const byte size = 2;
byte rates[size];
byte rateSpot = 0;
byte lastBeat = 0;
float BPM;
int beatAvg;

void setup()
{
    sensor.begin(Wire, I2C_SPEED_FAST);
}

void loop()
{

}