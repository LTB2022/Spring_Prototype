/**
 *  @filename   :   epd2in9_V2-demo.ino
 *  @brief      :   2.9inch e-paper V2 display demo
 *  @author     :   Yehui from Waveshare
 *
 *  Copyright (C) Waveshare     Nov 09 2020
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documnetation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to  whom the Software is
 * furished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include <SPI.h>
#include "epd2in9_V2.h"
#include "epdpaint.h"
#include "imagedata.h"

#define COLORED     0
#define UNCOLORED   1

/**
  * Due to RAM not enough in Arduino UNO, a frame buffer is not allowed.
  * In this case, a smaller image buffer is allocated and you have to 
  * update a partial display several times.
  * 1 byte = 8 pixels, therefore you have to set 8*N pixels at a time.
  */
unsigned char image[1024];
Paint paint(image, 0, 0);    // width should be the multiple of 8 
Epd epd;
unsigned long time_start_ms;
unsigned long time_now_s;

// this constant won't change:
const int  buttonPin = 14;    // the pin that the pushbutton is attached to
const int ledPin = 13;       // the pin that the LED is attached to

// Variables will change:
int buttonPushCounter = 0;   // counter for the number of button presses
int buttonState = 0;         // current state of the button
int lastButtonState = 0;     // previous state of the button

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);

  Serial.begin(115200);
  if (epd.Init() != 0) {
      Serial.print("e-Paper init failed");
      return;
  }
  
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(32);
  paint.SetHeight(200);

  /* For simplicity, the arguments are explicit numerical coordinates */

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Little Time", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Buddy", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 30, 100, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(2000);

  if (epd.Init() != 0) {
      Serial.print("e-Paper init failed ");
      return;
     
  }

  /** 
   *  there are 2 memory areas embedded in the e-paper display
   *  and once the display is refreshed, the memory area will be auto-toggled,
   *  i.e. the next action of SetFrameMemory will set the other memory area
   *  therefore you have to set the frame memory and refresh the display twice.
   */
  epd.SetFrameMemory_Base(IMAGE_DATA);
  epd.DisplayFrame();

  //time_start_ms = millis();

}

void loop() {
  // put your main code here, to run repeatedly:

  paint.SetWidth(32);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Home Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();
  
  // read the pushbutton input pin:
  buttonState = digitalRead(buttonPin);

  // compare the buttonState to its previous state
  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button went from off to on:
  paint.SetWidth(32);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "1st Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

    } else {
      // if the current state is LOW then the button went from on to off:
  paint.SetWidth(32);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "2nd Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();
    }
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state, for next time through the loop
  lastButtonState = buttonState;


  //////////////////////////////////////////////////////////////////////////////////////

  delay(180000);
}
