/** MADE BY GRIF **/

int val_btn_new, val_btn_old, val_pot,val_pot2;
bool stat_btn = true;
bool flag = false ;
void setup() {
  pinMode(pin_led, OUTPUT);
  String str;
  Serial.begin(9600);
  val_btn_old = 1;
}

void loop() {
  
    if (Serial.available()) {
      String str = Serial.readString();
      //Serial.println(str);
      if(str =="start"){
        flag = true;
      }
      if(str =="stop"){
        flag = false;
      }
      
    }if(flag){
      val_pot = analogRead(A0);
      val_pot2 = analogRead(A1);
      Serial.print(val_pot);
      Serial.print(",");
      Serial.println(val_pot2);
    }
    
      
    
    delay(100);
  

}
