/******************************************************************
 Created with PROGRAMINO IDE for Arduino - 23.01.2019 16:28:48
 Project     : Atomic synthesizer
 Libraries   :
 Author      : Mivallion
 Description : Mechanium project for ICAE
******************************************************************/


#ifndef LIGHT
#define LIGHT

Adafruit_NeoPixel protons = Adafruit_NeoPixel(indicatorNumPixels, protonsPin, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel electrons = Adafruit_NeoPixel(indicatorNumPixels, electronsPin, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel neutrons = Adafruit_NeoPixel(indicatorNumPixels, neutronsPin, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel led = Adafruit_NeoPixel(ledNumPixels, ledPin, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel symbols = Adafruit_NeoPixel(symbolsNumPixels, symbolsPin, NEO_GRB + NEO_KHZ800);

uint32_t currentColor, ColorNumber;

int dim_power = 10;
int dim_dir = 1;
uint32_t dim_timer = 0;
int animateIdx = 0;
int animateArr [] = {14,7,0,1,2,3,10,17,18,19};
unsigned long animateTimer = 100;
void animate() {
    for (int j = 0; j < 21; j++) {
        electrons.setPixelColor(j, electrons.Color(0, 0, 0));
        protons.setPixelColor(j, protons.Color(0, 0, 0));
        neutrons.setPixelColor(j, neutrons.Color(0, 0, 0));
    }
    if (animateIdx == 10) 
        animateIdx = 0;
    electrons.setPixelColor(animateArr[animateIdx], electrons.Color(0, 0, 255));
    protons.setPixelColor(animateArr[animateIdx], protons.Color(0, 255, 0));
    neutrons.setPixelColor(animateArr[animateIdx], neutrons.Color(255, 0, 0));
    animateIdx++; 
    electrons.show();
    protons.show();
    neutrons.show();
}

void dimmer_waiting(int t, int p) {
    if (dim_timer == 0) {
        dim_timer = millis();
    }
    uint32_t tmp_timer = millis();
    if (tmp_timer - dim_timer > t) {
        dim_timer = 0;
        if (dim_power == p)
            dim_dir = -1;
        else if (dim_power == 10)
            dim_dir = 1;
        dim_power += dim_dir;
        dimmer1.setPower(dim_power);
    }
}

void off7Segment() {
    for (int j = 0; j < 21; j++) {
        electrons.setPixelColor(j, electrons.Color(0, 0, 0));
        protons.setPixelColor(j, protons.Color(0, 0, 0));
        neutrons.setPixelColor(j, neutrons.Color(0, 0, 0));
    }
    electrons.show();
    protons.show();
    neutrons.show();
}
// el = e, n or p for electrons, neutrons or protons indicators
void display7Segment(char el) {
    switch (el) {
        case 'e':
            for (int j = 0; j <= 6; j++) {
                uint32_t currentColor;
                if (numbers[e % 10][j] > 0)
                    currentColor = electrons.Color(0, 0, 255);
                else
                    currentColor = electrons.Color(0, 0, 0);

                electrons.setPixelColor(j, currentColor);
            }
            for (int j = 7; j <= 13; j++) {
                uint32_t currentColor;

                if ((numbers[(e % 100) / 10 - 1][j] > 0) && (((e % 100) / 10 != 0) || ((e % 1000) / 100 != 0)))
                    currentColor = electrons.Color(0, 0, 255);
                else
                    currentColor = electrons.Color(0, 0, 0);
                electrons.setPixelColor(j, currentColor);
            }
            for (int j = 14; j <= 20; j++) {
                uint32_t currentColor;
                if ((numbers[(e % 1000) / 100 - 2][j] > 0) && ((e % 1000) / 100 != 0))
                    currentColor = electrons.Color(0, 0, 255);
                else
                    currentColor = electrons.Color(0, 0, 0);

                electrons.setPixelColor(j, currentColor);
            }
            electrons.show();
            break;
        case 'v':
            for (int j = 0; j <= 6; j++) {
                uint32_t currentColor;
                if (numbers[volume % 10][j] > 0)
                    currentColor = electrons.Color(0, 0, 255);
                else
                    currentColor = electrons.Color(0, 0, 0);

                electrons.setPixelColor(j, currentColor);
            }
            for (int j = 7; j <= 13; j++) {
                uint32_t currentColor;

                if ((numbers[(volume % 100) / 10 - 1][j] > 0) && (((volume % 100) / 10 != 0) || ((volume % 1000) / 100 != 0)))
                    currentColor = electrons.Color(0, 0, 255);
                else
                    currentColor = electrons.Color(0, 0, 0);
                electrons.setPixelColor(j, currentColor);
            }
            for (int j = 14; j <= 20; j++) {
                uint32_t currentColor;
                if ((numbers[(volume % 1000) / 100 - 2][j] > 0) && ((volume % 1000) / 100 != 0))
                    currentColor = electrons.Color(0, 0, 255);
                else
                    currentColor = electrons.Color(0, 0, 0);

                electrons.setPixelColor(j, currentColor);
            }
            electrons.show();
            break;

        case 'n':
            for (int j = 0; j <= 6; j++) {
                uint32_t currentColor;
                if (numbers[n % 10][j] > 0)
                    currentColor = neutrons.Color(0, 255, 0);
                else
                    currentColor = neutrons.Color(0, 0, 0);

                neutrons.setPixelColor(j, currentColor);
            }
            for (int j = 7; j <= 13; j++) {
                uint32_t currentColor;

                if ((numbers[(n % 100) / 10 - 1][j] > 0) && (((n % 100) / 10 != 0) || ((n % 1000) / 100 != 0)))
                    currentColor = neutrons.Color(0, 255, 0);
                else
                    currentColor = neutrons.Color(0, 0, 0);
                neutrons.setPixelColor(j, currentColor);
            }
            for (int j = 14; j <= 20; j++) {
                uint32_t currentColor;
                if ((numbers[(n % 1000) / 100 - 2][j] > 0) && ((n % 1000) / 100 != 0))
                    currentColor = neutrons.Color(0, 255, 0);
                else
                    currentColor = neutrons.Color(0, 0, 0);

                neutrons.setPixelColor(j, currentColor);
            }
            neutrons.show();
            break;

        case 'p':
            for (int j = 0; j <= 6; j++) {
                uint32_t currentColor;
                if (numbers[p % 10][j] > 0)
                    currentColor = protons.Color(255, 0, 0);
                else
                    currentColor = protons.Color(0, 0, 0);

                protons.setPixelColor(j, currentColor);
            }
            for (int j = 7; j <= 13; j++) {
                uint32_t currentColor;

                if ((numbers[(p % 100) / 10 - 1][j] > 0) && (((p % 100) / 10 != 0) || ((p % 1000) / 100 != 0)))
                    currentColor = protons.Color(255, 0, 0);
                else
                    currentColor = protons.Color(0, 0, 0);
                protons.setPixelColor(j, currentColor);
            }
            for (int j = 14; j <= 20; j++) {
                uint32_t currentColor;
                if ((numbers[(p % 1000) / 100 - 2][j] > 0) && ((p % 1000) / 100 != 0))
                    currentColor = protons.Color(255, 0, 0);
                else
                    currentColor = protons.Color(0, 0, 0);

                protons.setPixelColor(j, currentColor);
            }
            protons.show();
            break;

        default:

            break;
    }
}

void displaySymbols(int mode) {
    if (mode == 0) {
        symbols.setPixelColor(0, symbols.Color(0, 0, 0)); // n
        symbols.setPixelColor(1, symbols.Color(0, 0, 0)); // p
        symbols.setPixelColor(2, symbols.Color(0, 0, 0)); // e
    } else {
        symbols.setPixelColor(0, symbols.Color(0, 255, 0)); // n
        symbols.setPixelColor(1, symbols.Color(255, 0, 0)); // p
        symbols.setPixelColor(2, symbols.Color(0, 0, 255)); // e
    }
    symbols.show();
}

void displayLed(int mode) {
    if (mode == 0) {
        for (int i = 0; i < ledNumPixels; i++)
            led.setPixelColor(i, led.Color(0, 0, 0));
    } else {
        for (int i = 0; i < ledNumPixels; i++)
            led.setPixelColor(i, led.Color(255, 255, 255));
    }
    led.show();
}


void smoothLampsOn(int t, char c) {
    for (int i = dimmerMinPower; i < dimmerMaxPower; i++) {
        dimmer1.setPower(i);
        for (int j = 0; j < ledNumPixels; j++)
            switch (c) {
                case 'g':
                    led.setPixelColor(j, led.Color(abs( i * 255 / dimmerMaxPower - i), 0, 0));
                    break;
                case 'r':
                    led.setPixelColor(j, led.Color(0, abs( i * 255 / dimmerMaxPower - i), 0));
                    break;
                default:

                    break;
            }
        analogWrite(nixiesPin, abs( i * 255 / dimmerMaxPower - i));
        led.show();
        if (animateTimer >= 100) {
            animateTimer = 0;
            animate();
        }
        delay(t);
        animateTimer+=t;
    }
}
void smoothLampsOff(int t, char c) {

    for (int i = dimmerMaxPower; i > dimmerMinPower; i--) {
        dimmer1.setPower(i);
        for (int j = 0; j < ledNumPixels; j++)
            switch (c) {
                case 'g':
                    led.setPixelColor(j, led.Color(abs( i * 255 / dimmerMaxPower - i), 0, 0));
                    break;
                case 'r':
                    led.setPixelColor(j, led.Color(0, abs( i * 255 / dimmerMaxPower - i), 0));
                    break;
                default:

                    break;
            }
        analogWrite(nixiesPin, abs( i * 255 / dimmerMaxPower - i));
        led.show();
        if (animateTimer >= 100) {
            animateTimer = 0;
            animate();
        }
        delay(t);
        animateTimer+=t;
    }
    analogWrite(nixiesPin, 0);
}

void delayAnimate(unsigned long t) {
    delay(100 - t);
    animate();
    delay(t);
}

void lightShow() {
    //off7Segment();
    smoothLampsOn(20, 'g');
    delayAnimate(animateTimer);
    smoothLampsOff(10, 'g');
    smoothLampsOn(10, 'g');
    delayAnimate(animateTimer);
    smoothLampsOff(20, 'g');
    smoothLampsOn(10, 'g');
    delayAnimate(animateTimer);
    smoothLampsOff(10, 'g');
    smoothLampsOn(20, 'g');
    delayAnimate(animateTimer);
    smoothLampsOff(10, 'g');
    smoothLampsOn(20, 'g');
    delayAnimate(animateTimer);
    smoothLampsOff(10, 'g');
    smoothLampsOn(20, 'g');
    delayAnimate(animateTimer);
    smoothLampsOff(10, 'g');
    smoothLampsOn(20, 'g');
    delayAnimate(animateTimer);
    smoothLampsOff(10, 'g');
    displayLed(0);
    animateIdx = 0;
    animateTimer = 0;
    off7Segment();
}

void alertLightShow() {
    //off7Segment();
    smoothLampsOn(20, 'r');
    delay(50);
    smoothLampsOff(10, 'r');
    delay(50);
    smoothLampsOn(20, 'r');
    delay(50);
    smoothLampsOff(10, 'r');
}

void ledSetup() {
    led.begin();
    symbols.begin();
    electrons.begin();
    neutrons.begin();
    protons.begin();
    //dimmer1.begin(NORMAL_MODE, OFF);
    //dimmer1.setPower(50); // setPower(0-100%);
    //dimmer1.setState(ON);
    off7Segment();
    displaySymbols(0);
    displayLed(0);
    //pinMode(zeroPin, INPUT);                 // РЅР°СЃС‚СЂР°РёРІР°РµРј РїРѕСЂС‚ РЅР° РІС…РѕРґ РґР»СЏ РѕС‚СЃР»РµР¶РёРІР°РЅРёСЏ РїСЂРѕС…РѕР¶РґРµРЅРёСЏ СЃРёРіРЅР°Р»Р° С‡РµСЂРµР· РЅРѕР»СЊ
    // attachInterrupt(0, detect_up, FALLING);  // РЅР°СЃС‚СЂРѕРёС‚СЊ СЃСЂР°Р±Р°С‚С‹РІР°РЅРёРµ РїСЂРµСЂС‹РІР°РЅРёСЏ interrupt0 РЅР° pin 2 РЅР° РЅРёР·РєРёР№ СѓСЂРѕРІРµРЅСЊ
    //StartTimer1(timer_interrupt, 40);        // РІСЂРµРјСЏ РґР»СЏ РѕРґРЅРѕРіРѕ СЂР°Р·СЂСЏРґР° РЁР�Рњ
    //StopTimer1();

    pinMode(nixiesPin, OUTPUT);
    Serial.println("LIGHT LAUNCH SUCCESSFULL");
}

#endif
