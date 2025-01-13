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
    delay(5000);

    digitalWrite(pin, LOW);
    Serial.println("LED Off!");
    delay(1000);
}