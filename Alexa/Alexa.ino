int buzzer = 11; //buzzer to arduino pin 9

void setup() {
  // put your setup code here, to run once:
  pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output
  pinMode(13, OUTPUT); //Uses onboard led, Shines whilst buzzer is bleeping
  Serial.begin(9600);//Starts Serial
  Serial.println("Start");
}
int x = 0;
void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Yeet");
  Serial.println(x);
  x = x + 1;
}
