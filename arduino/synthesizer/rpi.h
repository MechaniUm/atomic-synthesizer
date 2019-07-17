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
    for (int i = 0; i < rpiPinsCount; i++)
    {
        pinMode(rpiPins[i], INPUT);
    }
    Serial.println("RPI LAUNCH SUCCESSFULL");
}

int rpiGetSignal() {
    while (digitalRead(rpiPins[0]) != HIGH)
        delay(10);
    return ((digitalRead(rpiPins[1]) == HIGH) ? 1 : 0);
}

#endif
