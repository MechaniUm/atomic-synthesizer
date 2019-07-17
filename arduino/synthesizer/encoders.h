/******************************************************************
 Created with PROGRAMINO IDE for Arduino - 23.01.2019 18:01:19
 Project     : Atomic synthesizer
 Libraries   :
 Author      : Mivallion
 Description : Mechanium project for ICAE
******************************************************************/

#ifndef ENCODERS
#define ENCODERS

void displayNewObj() {
    if (new_obj) {
        new_obj = false;
        newObjectEventJSON();
    }
}

void encodersSetup() {
    for (int i = 0; i < 6; i++) {
        pinMode(encoderPins[i], INPUT);
    }
    Serial.println("ENCODERS LAUNCH SUCCESSFULL");
}

void readEncoders() {
    // protons
    n0 = digitalRead(encoderPins[0]);
    if ((encoder0PinALast == LOW) && (n0 == HIGH)) {
        unsigned long curTime = millis();
        if ((curTime - encoderCounterTimer < timeForEncoderCounter) || (encoderCounterTimer == 0)) {
            if (digitalRead(encoderPins[1]) == LOW) {
                if (encoderDirection == 0) {
                    encoderCounterTimer = millis();
                    encoderDirection = -1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else if (encoderDirection != -1) {
                    encoderDirection = -1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else {
                    encoderCounter++;
                    if (encoderCounter == encoderCounterLimit) {
                        encoderCounter = 0;
                        encoderDirection = 0;
                        encoderCounterTimer = 0;
                        if (n > 0) {
                            n--;
                            updateTimer();
                            displayNewObj();
                            display7Segment('n');
                        }
                    }
                }
            } else {
                if (encoderDirection == 0) {
                    encoderCounterTimer = millis();
                    encoderDirection = 1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else if (encoderDirection != 1) {
                    encoderDirection = 1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else {
                    encoderCounter++;
                    if (encoderCounter == encoderCounterLimit) {
                        encoderCounter = 0;
                        encoderDirection = 0;
                        encoderCounterTimer = 0;
                        if (n < 255) {
                            n++;
                            updateTimer();
                            displayNewObj();
                            display7Segment('n');
                        }
                    }
                }
            }
        } else {
            encoderCounter = 0;
            encoderDirection = 0;
            encoderCounterTimer = 0;
        }
    }
    encoder0PinALast = n0;
    //electrons and volume
    n1 = digitalRead(encoderPins[2]);
    if ((encoder1PinALast == LOW) && (n1 == HIGH)) {
        unsigned long curTime = millis();
        if ((curTime - encoderCounterTimer < timeForEncoderCounter) || (encoderCounterTimer == 0)) {
            if (digitalRead(encoderPins[3]) == LOW) {
                if (encoderDirection == 0) {
                    encoderCounterTimer = millis();
                    encoderDirection = -1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else if (encoderDirection != -1) {
                    encoderDirection = -1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else {
                    encoderCounter++;
                    if (encoderCounter == encoderCounterLimit) {
                        if (buttonPressed[0] == 1) {
                            if (volume > 0) {
                                volume--;
                                display7Segment('v');
                                volumeEventJSON();
                            }
                        } else {
                            if (e > 0) {
                                e--;
                                display7Segment('e');
                            }
                        }
                        updateTimer();
                        displayNewObj();
                        encoderCounter = 0;
                        encoderDirection = 0;
                        encoderCounterTimer = 0;

                    }
                }
            } else {
                if (encoderDirection == 0) {
                    encoderCounterTimer = millis();
                    encoderDirection = 1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else if (encoderDirection != 1) {
                    encoderDirection = 1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else {
                    encoderCounter++;
                    if (encoderCounter == encoderCounterLimit) {
                        encoderCounter = 0;
                        encoderDirection = 0;
                        encoderCounterTimer = 0;
                        updateTimer();
                        displayNewObj();
                        if (buttonPressed[0] == 1) {
                            if (volume < 100) {
                                volume++;
                                display7Segment('v');
                                volumeEventJSON();
                            }
                        } else {
                            if (e < 255) {
                                e++;
                                display7Segment('e');
                            }
                        }
                    }
                }
            }
        } else {
            encoderCounter = 0;
            encoderDirection = 0;
            encoderCounterTimer = 0;
        }
    }
    encoder1PinALast = n1;
    // protons
    n2 = digitalRead(encoderPins[4]);
    if ((encoder2PinALast == LOW) && (n2 == HIGH)) {
        unsigned long curTime = millis();
        if ((curTime - encoderCounterTimer < timeForEncoderCounter) || (encoderCounterTimer == 0)) {
            if (digitalRead(encoderPins[5]) == LOW) {
                if (encoderDirection == 0) {
                    encoderCounterTimer = millis();
                    encoderDirection = -1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else if (encoderDirection != -1) {
                    encoderDirection = -1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else {
                    encoderCounter++;
                    if (encoderCounter == encoderCounterLimit) {
                        encoderCounter = 0;
                        encoderDirection = 0;
                        encoderCounterTimer = 0;
                        if (p > 0) {
                            p--;
                            e = p;
                            updateTimer();
                            displayNewObj();
                            display7Segment('p');
                            display7Segment('e');
                        }
                    }
                }
            } else {
                if (encoderDirection == 0) {
                    encoderCounterTimer = millis();
                    encoderDirection = 1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else if (encoderDirection != 1) {
                    encoderDirection = 1;
                    encoderCounter = 0;
                    encoderCounterTimer = 0;
                } else {
                    encoderCounter++;
                    if (encoderCounter == encoderCounterLimit) {
                        encoderCounter = 0;
                        encoderDirection = 0;
                        encoderCounterTimer = 0;
                        if (p < 255) {
                            p++;
                            e = p;
                            updateTimer();
                            displayNewObj();
                            display7Segment('p');
                            display7Segment('e');
                        }
                    }
                }
            }
        } else {
            encoderCounter = 0;
            encoderDirection = 0;
            encoderCounterTimer = 0;
        }
    }
    encoder2PinALast = n2;
}


#endif
