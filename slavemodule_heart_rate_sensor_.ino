#define USE_ARDUINO_INTERRUPTS true     
#include <PulseSensorPlayground.h>     
#include <SoftwareSerial.h> 
SoftwareSerial s(5,6); 
const int PulseWire = 0; 
const int LED13 = 13;          
int Threshold = 550;                                                   
PulseSensorPlayground pulseSensor; 
void setup() {    
  Serial.begin(9600);          
  s.begin(9600); 
   pulseSensor.analogInput(PulseWire);      
   pulseSensor.blinkOnPulse(LED13);      
   pulseSensor.setThreshold(Threshold);    
   if (pulseSensor.begin()) { 
    Serial.println("We created a pulseSensor Object !");} 
} 

void loop() { 
  int myBPM = pulseSensor.getBeatsPerMinute();  
}
                                               
if (pulseSensor.sawStartOfBeat()) {            // Constantly test to see if "a beat happened".  
 Serial.println(“ A HeartBeat Happened ! "); // If test is "true", print a message "a heartbeat happened". 
 Serial.print("BPM: ");                        // Print phrase "BPM: "  
 Serial.println(myBPM);// Print the value inside of myBPM.  
 if(s.available()>0) 
{ 
 s.write(myBPM);}}   delay(20);                    // considered best practice in a simple sketch. 
} 
