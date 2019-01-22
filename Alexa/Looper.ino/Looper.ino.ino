int x = 0;
void setup() {
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  x = x + 1;
  Serial.println(x);
}
