const unsigned long SERIAL_BAUD_RATE = 9600; 
const int STATUS_LED = 13;

void setup() {
  pinMode(STATUS_LED, OUTPUT);
  Serial.begin(SERIAL_BAUD_RATE);
  // Removed while(!Serial) as it blocks non-native USB boards
  
  digitalWrite(STATUS_LED, HIGH);
  
  // Send an immediate heartbeat on startup
  delay(500); // Short stabilization delay
  Serial.println("DEVICE_ACTIVE");
}

void loop() {
  // Send regular heartbeat every 1 second
  Serial.println("DEVICE_ACTIVE");
  delay(1000);
}