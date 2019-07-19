/******************************************************************
 Created with PROGRAMINO IDE for Arduino - 23.01.2019 16:26:06
 Project     : Atomic synthesizer
 Libraries   :
 Author      : Mivallion
 Description : Mechanium project for ICAE
******************************************************************/


#ifndef SLEEP
#define SLEEP

void goToSleep() {
    if (!sleeping) {
        dimmer1.setPower(10);
        setSoundState(SOUND_OFF);
        digitalWrite(buttonLampPins[0], HIGH);
        digitalWrite(buttonLampPins[1], LOW);
        sleepEventJSON();
        sleeping = true;
        off7Segment();
        displaySymbols(0);
        displayLed(0);
        dim_timer = 0;
    }
}

void updateTimer() {
    lastActionTime = millis();
}

void checkTimer() {
    currentTime = millis();
    if (currentTime - lastActionTime > timeBeforeSleep & !sleeping) {
        goToSleep();
    }
}

#endif
