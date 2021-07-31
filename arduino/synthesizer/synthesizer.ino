/******************************************************************
 Created with PROGRAMINO IDE for Arduino - 23.01.2019 16:26:06
 Project         : Atomic synthesizer
 Libraries     :
 Author            : Mivallion
 Description : Mechanium project for ICAE
******************************************************************/
#include <Adafruit_NeoPixel.h>
#include <RBDdimmer.h>

#define ENCODER_DO_NOT_USE_INTERRUPTS
dimmerLamp dimmer1(6);

#include "properties.h"
#include "variables.h"
#include "json.h"
#include "audio.h"
#include "light.h"
#include "sleep.h"
#include "buttons.h"
#include "encoders.h"
#include "rpi.h"

int btn1Light = 0;

void info() {
    unsigned long tmp = millis();
    while (1) {
        currentTime = millis();
        if (currentTime - tmp > delayAfterSleep) {
            digitalWrite(buttonLampPins[0], LOW);
            btn1Light = 0;
            break;
        }
        else if (currentTime - tmp > timeBeforeSkip) {
            if (!btn1Light) {
                digitalWrite(buttonLampPins[0], HIGH);
                btn1Light = 1;
            }
            readButtons();
            if (buttonPressed[0]) {
                digitalWrite(buttonLampPins[0], LOW);
                btn1Light = 0;
                stopInfoEventJSON();
                break;
            }
        }
        delay(1);
    }
}


void wakeUp() {
    if (sleeping) {
        digitalWrite(buttonLampPins[0], LOW);
        wakeUpEventJSON();
        sleeping = false;
        e = 0;
        n = 0;
        p = 0;
        setSoundState(SOUND_ON);
        info();
        digitalWrite(buttonLampPins[1], HIGH);
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
    pinMode(buttonLamp1, OUTPUT);
    pinMode(buttonLamp2, OUTPUT);
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
            digitalWrite(buttonLampPins[0], LOW);
            buttonEventJSON(0); // text scroll
            delay(500);
            digitalWrite(buttonLampPins[0], HIGH);
        }
        if (buttonPressed[1]) {
            new_obj = true;
            delay(10);
            buttonEventJSON(1);
            digitalWrite(buttonLampPins[1], LOW);
            if (rpiGetSignal()) {
                lightShow();
                display7Segment('p');
                display7Segment('n');
                display7Segment('e');
                delay(delayAfterSynth);
                digitalWrite(buttonLampPins[0], HIGH);
            } else {
                alertLightShow();
                display7Segment('p');
                display7Segment('n');
                display7Segment('e');
            }
            digitalWrite(buttonLampPins[1], HIGH);
        }
        readEncoders();
        dimmer_waiting(50, 33);
    }
}
