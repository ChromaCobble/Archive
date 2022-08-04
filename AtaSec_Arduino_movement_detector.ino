 #define trig 11
 #define echo 10
 #define buzzer 9
 #define ldr A0
 int duration;
 int distanceCm;
 int distanceCm1;
 int ldrStatus;
 #define led 7
 #define brightled 4
 int movementcount = 0;
void setup()
{
  pinMode(ldr, INPUT);
  tone(buzzer,6000);
  delay(100);
  noTone(buzzer);
  pinMode(trig, OUTPUT);
  pinMode(brightled, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
  digitalWrite(led, HIGH);
  delay(100);
  digitalWrite(led,LOW);
  tone(buzzer,6000);
  delay(100);
  noTone(buzzer);
  delay(100);
  digitalWrite(led, HIGH);
  delay(100);
  digitalWrite(led,LOW);
  tone(buzzer,6000);
  delay(100);
  noTone(buzzer);
  delay(100);
  digitalWrite(led, HIGH);
  delay(100);
  digitalWrite(led,LOW);
  Serial.println("Deployed");
}

void loop()
{
  ldrStatus = analogRead(ldr);
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(2);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distanceCm=duration*0.034/2;
  Serial.print("CM:");
  Serial.println(distanceCm);
  
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(2);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distanceCm1=duration*0.034/2;
  Serial.print("CM:");
  Serial.println(distanceCm1);
  Serial.println(ldrStatus);
  if (ldrStatus >= 8)
  {
    Serial.println("Lights on");
    digitalWrite(brightled, HIGH);
    
  }
  else
  {
   digitalWrite(brightled, LOW); 
  }
  

   
    
  
  if (distanceCm1-distanceCm > 5){
    Serial.println("Movement detected");
    movementcount+=1;
    Serial.println("Registered moves:");
    Serial.println(movementcount);
    tone(buzzer, 3000);
    digitalWrite(led , HIGH);
    delay(500);
    tone(buzzer, 4000);
    delay(500);
    tone(buzzer, 3000);
    digitalWrite(led , HIGH);
    delay(500);
    tone(buzzer, 4000);
    delay(500);
    tone(buzzer, 3000);
    digitalWrite(led , HIGH);
    delay(500);
    tone(buzzer, 4000);
    delay(500);
    tone(buzzer, 3000);
    digitalWrite(led , HIGH);
    delay(500);
    tone(buzzer, 4000);
    delay(500);
    
    
    
  }
  else{
    noTone(buzzer);
    digitalWrite(led, LOW);
  }
  
  
  

   
  
}
