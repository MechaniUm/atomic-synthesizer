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
        sleepEventJSON();
        sleeping = true;
        off7Segment();
        displaySymbols(0);
        displayLed(0);
    }
}

//void wakeUp() {
//    if (sleeping) {
//        wakeUpEventJSON();
//        sleeping = false;
//        setSoundState(SOUND_ON);
//        delay(delayAfterSleep);
//        setSoundState(SOUND_OFF);
//    }
//}

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
