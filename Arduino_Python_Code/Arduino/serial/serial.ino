long num;
void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  num = random(60,150)
  Serial.println(num);
  delay(100);
}
