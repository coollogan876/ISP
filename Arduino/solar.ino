int solar = 1;
int prevRead = 0;
int current = 0;
int motorFwd = 7;
int motorRev = 8;
int tolerance = 25; 

void setup()
{
    Serial.begin(9600);
    pinMode(motorFwd, OUTPUT);
    pinMode(motorRev, OUTPUT);
    pinMode(solar, INPUT);
}

void loop()
{
    prevRead = analogRead(solar);
    Serial.println(prevRead);
    delay(250);
    current = analogRead(solar);
    if (current < prevRead - tolerance)
    {
        digitalWrite(motorFwd, HIGH);
        digitalWrite(motorRev, LOW);
    }
    else if (current > prevRead + tolerance)
    {
        digitalWrite(motorFwd, LOW);
        digitalWrite(motorRev, HIGH);
    }
    else 
    {
        digitalWrite(motorFwd, LOW);
        digitalWrite(motorRev, LOW);
    }
}
