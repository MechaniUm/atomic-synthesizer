/******************************************************************
 Created with PROGRAMINO IDE for Arduino - 23.01.2019 16:26:35
 Project     : Atomic synthesizer
 Libraries   :
 Author      : Mivallion
 Description : Mechanium project for ICAE
******************************************************************/


#ifndef PROPERTIES
#define PROPERTIES
#include <Arduino.h>
#include <Encoder.h>
#define timeForEncoderCounter 150
#define encoderCounterLimit 2
#define protonsPin 11
#define electronsPin 13
#define neutronsPin 12
#define indicatorNumPixels 22
#define ledPin 4
#define symbolsPin 10
#define nixiesCount 3
#define dimmerPin 3
#define dimmerMaxPower 40
#define dimmerMinPower 10
#define infoButtonPin 8
#define synthButtonPin 9
#define buttonLamp1 5
#define buttonLamp2 7
#define ledNumPixels 31
#define symbolsNumPixels 3
#define lightshowTime 2
#define alertLightshowTime 0.2
#define timeBeforeSleep 50000
#define mutePin 10
#define delayAfterSleep 22000
#define rpiPinsCount 4
#define delayAfterSynth 5000
#define timeBeforeSkip 5000
#define animateTick 100
#define encoder_step 12
const int buttonPins[] = { synthButtonPin, infoButtonPin };
const int buttonLampPins[] = { buttonLamp1, buttonLamp2 };
const int numbers[10][7] = {
    {1, 1, 1, 1, 1, 1, 0}, //0
    {0, 1, 1, 0, 0, 0, 0}, //1
    {1, 1, 0, 1, 1, 0, 1}, //2
    {1, 1, 1, 1, 0, 0, 1}, //3
    {0, 1, 1, 0, 0, 1, 1}, //4
    {1, 0, 1, 1, 0, 1, 1}, //5
    {1, 0, 1, 1, 1, 1, 1}, //6
    {1, 1, 1, 0, 0, 0, 0}, //7
    {1, 1, 1, 1, 1, 1, 1}, //8
    {1, 1, 1, 1, 0, 1, 1}  //9
};
const int animateArr [] = {15,8,1,2,3,4,11,18,19,20};
const int rpiPins[] = {39, 41};
const int nixiesPins[] = {14, 15, 16};
//const int encoderPins[] = { 33, 31, 25, 23, 27, 29 };
const int encoderPins[] = {24, 25, 26, 27, 22, 23};

Encoder encoder_n(25, 24);
Encoder encoder_e(27, 26);
Encoder encoder_p(23, 22);
#endif
