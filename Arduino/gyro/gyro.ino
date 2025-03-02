int x = 0;
int y = 1;
int z = 2;
void setup() {
  pinMode(x, INPUT);
  pinMode(y, INPUT);
  pinMode(z, INPUT);
  Serial.begin(9600);
}

void loop() {
   Serial.print("X: ");
   Serial.print(analogRead(x));
   Serial.print(" Y: ");
   Serial.print(analogRead(y));
   Serial.print(" Z: ");
  Serial.print(analogRead(z));
   Serial.println();
   delay(200);
}
