void setup(){   
    pinMode(13, OUTPUT);              
}
void loop(){
      for (int p=0; p<3; p=p+1){
         digitalWrite(13, HIGH);
         delay(500);
         digitalWrite(13, LOW);
         delay(500);}
      for (int p=0; p<3; p=p+1){
         digitalWrite(13, HIGH);
         delay(1000);
         digitalWrite(13, LOW);
         delay(500);}
      for (int p=0; p<3; p=p+1){
         digitalWrite(13, HIGH);
         delay(500);
         digitalWrite(13, LOW);
         delay(500);}
      delay(3000);
}
