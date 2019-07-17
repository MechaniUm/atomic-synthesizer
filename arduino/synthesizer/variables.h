/******************************************************************
 Created with PROGRAMINO IDE for Arduino - 23.01.2019 16:30:27
 Project     : Atomic synthesizer
 Libraries   :
 Author      : Mivallion
 Description : Mechanium project for ICAE
******************************************************************/


#ifndef VARIABLES
#define VARIABLES

unsigned long currentTime, lastActionTime = 0;
int e = 0, n = 0, p = 0, volume = 100;
int n0 = LOW, n1 = LOW, n2 = LOW;
int encoder0PinALast, encoder1PinALast, encoder2PinALast;
unsigned long encoderCounterTimer = 0;
int encoderCounter = 0;
int encoderDirection = 0;
bool sleeping = false;
int buttonPressed[] = { 0, 0 };
int buttonStates[] = { 0, 0 };
bool volumeChanged = false;
bool new_obj = true;
bool first = true;
bool tmp_bool = false;
bool tmp_bool_1 = false;


#endif
