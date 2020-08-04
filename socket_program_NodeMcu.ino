#include <SoftwareSerial.h> 
#include <ESP8266WiFi.h> 
#include "ThingSpeak.h" 
const char* ssid = "nachi"; 
const char* password= "123456789"; 
 
WiFiClient client; 
unsigned long chno=871063; 
const char* api="4DLU2VQS8BF3YCZB"; 
SoftwareSerial s(D6,D5); 
int data; 
void setup() { 
s.begin(9600); 
  Serial.begin(9600); 
  Serial.println(); 
  WiFi.begin(ssid,password);    
  ThingSpeak.begin(client);
  } 
void loop() { 
  s.write("s");   if (s.available()>0) 
  { 
    data=s.read(); 
    Serial.println(data); 
    ThingSpeak.writeField(chno,1,data,api);
    } 
}
