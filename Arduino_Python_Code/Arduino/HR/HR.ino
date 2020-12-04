int HR;
//long milis;
//String data;
void setup() {
  Serial.begin(9600);
  //data.reserve(100);
}

void loop() {
  HR=analogRead(0);
  /*milis=millis();
  data="HR:";
  data+=HR;
  data+=" ML:";
  data+=milis;*/
  Serial.println(HR);
}
