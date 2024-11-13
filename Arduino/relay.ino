int relay = 7;

void setup()
{
	pinMode(relay, OUTPUT);
    digitalWrite(relay, LOW);
    Serial.begin(9600);
}

void loop()
{
	if (Serial.available() > 0)
    {
        char command = Serial.read();
        if (command == '1')
        {
            digitalWrite(relay, HIGH);
            Serial.write("on");
        }
        else if (command == '0')
        {
            digitalWrite(relay, LOW);
            Serial.write("off");
        }
    }
}
