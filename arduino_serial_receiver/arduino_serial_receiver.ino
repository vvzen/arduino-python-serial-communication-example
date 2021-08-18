#define LED_PIN 13

const byte MESSAGE_MAX_LENGTH = 32;
char currentMessage[MESSAGE_MAX_LENGTH];

const int END_MESSAGE_DELIMITER = 0x3F; // '>' char delimiter

void setup() {
  Serial.begin(9600);

  // Just to do some flashy blinking
  pinMode(LED_PIN, OUTPUT);
}

void loop() {

  digitalWrite(LED_PIN, LOW);

  if (Serial.available() > 0) {

    // Refill the buffer with nulls
    for (int i = 0; i < MESSAGE_MAX_LENGTH; i++){
      currentMessage[i] = '\0';
    }

    // Read into buffer
    Serial.readBytesUntil(END_MESSAGE_DELIMITER, currentMessage, MESSAGE_MAX_LENGTH);

    // Write back
    digitalWrite(LED_PIN, HIGH);
    for (int i = 0; i < MESSAGE_MAX_LENGTH; i++){
      if (currentMessage[i] != '\0') {
        Serial.write(currentMessage[i]);
      }
    }
    digitalWrite(LED_PIN, LOW);

  }
}
