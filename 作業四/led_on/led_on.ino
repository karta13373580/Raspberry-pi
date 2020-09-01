int pyrequir =0;
int led = 0;
void setup(){
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    pyrequir = Serial.read();
    if (pyrequir == 49){
      digitalWrite(13, HIGH);
      delay(1000);
    }
    else if(pyrequir == 50){
      digitalWrite(13, LOW);
      delay(1000);
    }
  }
}
