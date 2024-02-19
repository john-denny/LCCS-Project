// Define PIR sensor pin
const int pirSensorPin = 8; // Change this if you connected the sensor to a different pin

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Initialize PIR sensor pin as INPUT
  pinMode(pirSensorPin, INPUT);
  // Serial.println("00"); // Debug symbol that won't fuck with the 
}

void loop() {
  // Read the state of the PIR sensor
  int pirState = digitalRead(pirSensorPin);

  // Print the PIR sensor state to the serial monitor
  Serial.println(pirState);
  // Add a short delay to avoid flooding the serial monitor
  delay(100);
}
