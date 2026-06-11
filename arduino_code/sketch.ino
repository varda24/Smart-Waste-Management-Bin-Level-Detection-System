#define TRIG_PIN 5
#define ECHO_PIN 18

#define GREEN_LED 26
#define RED_LED 27
#define BUZZER 25

const float BIN_HEIGHT = 30.0; // Bin height in cm

float getDistance() {

  // Send trigger pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);

  digitalWrite(TRIG_PIN, LOW);

  // Read echo pulse
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  // Timeout protection
  if (duration == 0) {
    return BIN_HEIGHT;
  }

  float distance = duration * 0.034 / 2.0;

  // Prevent unrealistic values
  if (distance > BIN_HEIGHT) {
    distance = BIN_HEIGHT;
  }

  if (distance < 0) {
    distance = 0;
  }

  return distance;
}

void setup() {

  Serial.begin(115200);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);

  pinMode(BUZZER, OUTPUT);

  Serial.println("================================");
  Serial.println("SMART WASTE MANAGEMENT SYSTEM");
  Serial.println("================================");
}

void loop() {

  float distance = getDistance();

  float fillPercent =
      ((BIN_HEIGHT - distance) / BIN_HEIGHT) * 100.0;

  fillPercent = constrain(fillPercent, 0, 100);

  String status;
  String alertStatus;

  // Empty to Half Full
  if (fillPercent < 50) {

    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(RED_LED, LOW);

    noTone(BUZZER);

    status = "EMPTY";
    alertStatus = "NO ALERT";
  }

  // Half Full
  else if (fillPercent < 80) {

    digitalWrite(GREEN_LED, LOW);
    digitalWrite(RED_LED, HIGH);

    noTone(BUZZER);

    status = "HALF FULL";
    alertStatus = "MONITOR";
  }

  // Full
  else {

    digitalWrite(GREEN_LED, LOW);
    digitalWrite(RED_LED, HIGH);

    tone(BUZZER, 1000);

    status = "FULL";
    alertStatus = "COLLECTION REQUIRED";
  }

  Serial.println("--------------------------------");
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  Serial.print("Fill Level: ");
  Serial.print(fillPercent);
  Serial.println(" %");

  Serial.print("Status: ");
  Serial.println(status);

  Serial.print("Alert: ");
  Serial.println(alertStatus);

  delay(2000);
}