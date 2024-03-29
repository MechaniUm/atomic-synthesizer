/******************************************************************
 Created with PROGRAMINO IDE for Arduino - 23.01.2019 16:26:06
 Project         : Atomic synthesizer
 Libraries     :
 Author            : Mivallion
 Description : Mechanium project for ICAE
******************************************************************/
#include <Adafruit_NeoPixel.h>
#include <RBDdimmer.h>

dimmerLamp dimmer1(3);

#include "properties.h"
#include "variables.h"
#include "json.h"
#include "audio.h"
#include "light.h"
#include "sleep.h"
#include "buttons.h"
#include "encoders.h"
#include "rpi.h"

void info() {
    unsigned long tmp = millis();
    while (1) {
        currentTime = millis();
        if (currentTime - tmp > delayAfterSleep) {
            //digitalWrite(buttonLampPins[0], LOW);
            //btn1Light = 0;
            break;
        }
        else if (currentTime - tmp > timeBeforeSkip) {
            //if (!btn1Light) {
                //digitalWrite(buttonLampPins[0], HIGH);
                //btn1Light = 1;
            //}
            readButtons();
            if (buttonPressed[0]) {
                //digitalWrite(buttonLampPins[0], LOW);
                //btn1Light = 0;
                stopInfoEventJSON();
                break;
            }
        }
        delay(1);
    }
}


void wakeUp() {
    if (sleeping) {
        //digitalWrite(buttonLampPins[0], LOW);
        wakeUpEventJSON();
        sleeping = false;
        e = 0;
        n = 0;
        p = 0;

        setSoundState(SOUND_ON);
        // delay(delayAfterSleep);
        info();
        //digitalWrite(buttonLampPins[1], HIGH);
        setSoundState(SOUND_OFF);
    }
}

void setup()
{
    Serial.begin(9600);
    dimmer1.begin(NORMAL_MODE, OFF);
    dimmer1.setPower(10); // setPower(0-100%);
    dimmer1.setState(ON);
    soundSetup();
    ledSetup();
    buttonsSetup();
    encodersSetup();
    rpiSetup();
    setSoundState(SOUND_OFF);
    Serial.println("SYSTEM LAUNCH SUCCESSFULL");
    Serial.println("GOING TO SLEEP");
    goToSleep();
}

void loop()
{
    readButtons();
    if (buttonPressed[0] && sleeping) {
        wakeUp();
        displaySymbols(1);
        e = 0;
        n = 0;
        p = 0;
        display7Segment('p');
        display7Segment('n');
        display7Segment('e');
    }
    if (!sleeping) {
        checkTimer();
        if (buttonPressed[0] && new_obj) {
            delay(10);
            buttonEventJSON(0); // text scroll
            delay(500);
        }
        if (buttonPressed[1]) {
            new_obj = true;
            delay(10);
            buttonEventJSON(1);
            if (rpiGetSignal()) {
                //off7Segment();
                //displaySymbols(0);
                setSoundState(SOUND_ON);
                lightShow();
                display7Segment('p');
                display7Segment('n');
                display7Segment('e');
                setSoundState(SOUND_OFF);
                delay(delayAfterSynth);
                //displaySymbols(1);
            } else {
                setSoundState(SOUND_ON);
                alertLightShow();
                setSoundState(SOUND_OFF);
                display7Segment('p');
                display7Segment('n');
                display7Segment('e');
                displaySymbols(1);
            }
        }
        readEncoders();
        dimmer_waiting(50, 33);
    }
}
