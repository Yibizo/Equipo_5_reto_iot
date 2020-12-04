int del;

void setup() {
  del = 1000;
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(del);
  digitalWrite(LED_BUILTIN, LOW);
  delay(del);

}
