// Blink Program For Arduino UNO 

#define pin 13

void setup()
{
  pinMode(pin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
    digitalWrite(pin, HIGH);
    Serial.println("LED On!");
    delay(2000);

    digitalWrite(pin, LOW);
    Serial.println("LED Off!");
    delay(500);
}