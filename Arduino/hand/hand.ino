#include <map>
#include <string>
#include <thread>

int button = 1;

std::map<int, int> values;
std::map<int, int> zeros;

void setup()
{
    Serial.Begin(9600); 
    pinMode(button, INPUT);
    for (int x = 0; x < 5; x++)
    {
        pinMode(x, INPUT);
        values.insert(x, 0);
        zeros.insert(x, 0);
    }
    zero();
    std::thread valuesThread(valueUpdate);
}

void zero()
{
    for (int x = 0; x < values.size(); x++)
    {
        zero.at(x) = value.at(x);
    }
}

void valueUpdate()
{
    for (int x = 0; x < values.size(); x++)
    {
        values.at(x) = analogRead(x);
    }
}

void loop()
{
  std::string finger;
  if (digitalRead(button) == HIGH)
  {
    zero();
  }

  for (int x = 0; x < values.size(); x++)
  {
    switch(x)
    {
        case 0:
        {
            finger = "thumb"
            break;
        }
        case 1:
        {
            finger = "index";
            break;
        }
        case 2:
        {
            finger = "middle";
            break;
        }
        case 3:
        {
            finger = "ring";
            break;
        }
        case 4:
        {
            finger = "pinky";
            break;
        }
    }
    Serial.print(finger + " " + (values.at(x). - zeros.at(x)));
    Serial.println();
  }

  delay(.25);
}