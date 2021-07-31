/******************************************************************
 Created with PROGRAMINO IDE for Arduino - 23.01.2019 16:26:06
 Project     : Atomic synthesizer
 Libraries   :
 Author      : Mivallion
 Description : Mechanium project for ICAE
******************************************************************/


#ifndef RPI
#define RPI

void rpiSetup() {
    signal = "";
    do {
      signal = Serial.readString();
      Serial.println(signal);
    } while (!signal.equals("1\n"));
    Serial.println("RPI LAUNCH SUCCESSFULL");
}

int rpiGetSignal() {
    signal = "";
    do {
      signal = Serial.readString();
    } while (!signal.equals("1\n") && !signal.equals("0\n"));
        
    Serial.write("{\"event\": \"readed\"}\n");
    return (signal.equals("1\n") ? 1 : 0);
}

#endif
