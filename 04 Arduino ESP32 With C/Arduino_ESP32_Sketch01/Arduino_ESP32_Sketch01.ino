void setup() {
    Serial.begin(115200);  // Start Serial communication at 115200 baud
}

void loop() {
    Serial.println("Hello, World!");  // Print message to Serial Monitor
    delay(1000);  // Wait for 1 second
}