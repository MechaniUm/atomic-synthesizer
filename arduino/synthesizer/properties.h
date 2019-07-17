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
#define timeForEncoderCounter 150
#define encoderCounterLimit 2
#define protonsPin 15
#define electronsPin 14
#define neutronsPin 16
#define indicatorNumPixels 21
#define ledPin 19
#define symbolsPin 17
#define nixiesPin 5
#define dimmerPin 3
#define dimmerMaxPower 40
#define dimmerMinPower 10
#define infoButtonPin 35
#define synthButtonPin 37
#define ledNumPixels 3
#define symbolsNumPixels 3
#define lightshowTime 2
#define alertLightshowTime 0.2
#define timeBeforeSleep 30000
#define mutePin 4
#define delayAfterSleep 22000
#define rpiPinsCount 4
#define delayAfterSynth 10000
#define timeBeforeSkip 5000
#define animateTick 100
const int buttonPins[] = { infoButtonPin, synthButtonPin };
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
const int rpiPins[] = {39, 41};
// x x p
const int encoderPins[] = { 33, 31, 25, 23, 27, 29 };
#endif
