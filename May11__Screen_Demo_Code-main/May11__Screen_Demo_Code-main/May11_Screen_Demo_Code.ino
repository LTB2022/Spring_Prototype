//--------------------------------------------------------------------------------------------------

#include <SPI.h>
#include "epd2in9_V2.h"
#include "epdpaint.h"
#include "EasterEggLogo.h"
#include "EasterEgg.h"
#include "Neal.h"
#include "Record.h"

// pin definitions-----------------------------------------------------------------------------------

#define COLORED        0
#define UNCOLORED      1
const int HomePin       = 13;
const int Profile1Pin   = 14;
const int Tracking1Pin  = 15;
const int Focus1Pin     = 16;
const int Profile2Pin   = 17;
const int VoiceNotePin  = 18;
const int RecordPin     = 19;

//--------------------------------------------------------------------------------------------------

unsigned char image[1024];
Paint paint(image, 0, 0);    // width should be the multiple of 8 
Epd epd;
unsigned long time_start_ms;
//unsigned long time_now_s;

//--------------------------------------------------------------------------------------------------

void setup() {
  
  Serial.begin(115200);
  if (epd.Init() != 0) {
      Serial.print("e-Paper init failed");
      return;
  }

  pinMode(HomePin, INPUT_PULLDOWN);
  pinMode(Profile1Pin, INPUT_PULLDOWN);
  pinMode(Tracking1Pin, INPUT_PULLDOWN);  
  pinMode(Focus1Pin, INPUT_PULLDOWN);
  pinMode(Profile2Pin, INPUT_PULLDOWN);
  pinMode(VoiceNotePin, INPUT_PULLDOWN);
  pinMode(RecordPin, INPUT_PULLDOWN);

  attachInterrupt(digitalPinToInterrupt(HomePin), Home, RISING);
  attachInterrupt(digitalPinToInterrupt(Profile1Pin), Profile1, RISING);
  attachInterrupt(digitalPinToInterrupt(Tracking1Pin), Tracking1, RISING);
  attachInterrupt(digitalPinToInterrupt(Focus1Pin), Focus1, RISING);
  attachInterrupt(digitalPinToInterrupt(Profile2Pin), Profile2, RISING);
  attachInterrupt(digitalPinToInterrupt(VoiceNotePin), VoiceNote, RISING);
  attachInterrupt(digitalPinToInterrupt(RecordPin), Record, RISING);

  
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(32);
  paint.SetHeight(200);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "Little Time", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 64, 56, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "Buddy", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 40, 96, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();


  if (epd.Init() != 0) {
      Serial.print("e-Paper init failed ");
      return; 
  }

}

//--------------------------------------------------------------------------------------------------

void loop() {
  
}
//--------------------------------------------------------------------------------------------------
//States//
// NOTE: All values for sizing and locations are set in increments of 8-bits. 
void Home(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetWidth(24);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "LITTLE", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 8, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "TIME", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 48, 8, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "BUDDY", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 0, 8, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "PROFILE 1", &Font20, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 168, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "PROFILE 2", &Font20, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 48, 168, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  
  delay(180000);
}

void Profile1(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetWidth(24);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

 
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "PROFILE 1", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 8, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  
  
  paint.DrawStringAt(0, 4, "TRACKING", &Font20, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 180, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "FOCUS", &Font20, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 48, 220, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();
  delay(180000);
}

void Tracking1(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetWidth(24);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "TRACKING 1", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 8, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "VOICE NOTE", &Font20, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 154, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "RETURN HOME", &Font20, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 48, 140, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();
  delay(180000);
 
}

void Focus1(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  epd.SetFrameMemory_Base(Easter_Egg_Logo);
  epd.DisplayFrame();
  
  epd.SetFrameMemory_Base(Easter_Egg);
  time_start_ms = millis();
 
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(16);
  paint.SetHeight(200);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(8, 4, "AHH AHH AHH AHH AHH AHH", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 64, 124, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(8, 4, "AHH AHH AHH AHH AHH AHH", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 48, 124, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(8, 4, "AHH AHH AHH AHH AHH AHH", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 32, 124, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(8, 4, "AHH AHH AHH AHH AHH AHH", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 16, 124, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(8, 4, "AHH AHH AHH AHH AHH AHH", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 0, 124, paint.GetWidth(), paint.GetHeight());
  
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(24);
  paint.SetHeight(160);
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "FOCUS TIMER", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 160, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "IN DEVELOPMENT", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 80, 140, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();
 
  delay(180000);
}

void Profile2(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetWidth(24);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "PROFILE 2", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 8, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "TRACKING", &Font20, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 96, 180, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "FOCUS", &Font20, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 48, 220, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();
  delay(180000);
}

void VoiceNote(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  epd.SetFrameMemory_Base(Neal_Data);
  time_start_ms = millis();

  paint.SetRotate(ROTATE_90);
  paint.SetWidth(24);
  paint.SetHeight(200);
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "LEAVE A VOICE NOTE", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 104, 96, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "YES", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 88, 260, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "NO", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 48, 270, paint.GetWidth(), paint.GetHeight());

  paint.SetRotate(ROTATE_90);
  paint.SetWidth(16);
  paint.SetHeight(144);
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "You can do it", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 32, 148, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "either or both", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 16, 148, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "ways -Neal", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 0, 148, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();
  delay(180000);
}

void Record(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  epd.SetFrameMemory_Base(Record_State);
  time_start_ms = millis();
 
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(16);
  paint.SetHeight(160);
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "RECORDING DATA", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 112, 136, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "Return Home", &Font16, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 88, 176, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "Time...", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 48, 132, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "Is on", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 32, 132, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "Your side", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 16, 132, paint.GetWidth(), paint.GetHeight());
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(0, 4, "Yes it is", &Font12, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 0, 132, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();
  
  delay(180000);
}
