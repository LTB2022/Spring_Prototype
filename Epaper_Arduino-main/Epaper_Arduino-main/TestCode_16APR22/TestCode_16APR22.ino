//--------------------------------------------------------------------------------------------------

#include <SPI.h>
#include "epd2in9_V2.h"
#include "epdpaint.h"
#include "imagedata.h"

// pin definitions-----------------------------------------------------------------------------------

#define COLORED        0
#define UNCOLORED      1
const int HomePin       = 4;
const int Profile1Pin   = A0;
const int Tracking1Pin  = A1;
const int Focus1Pin     = A2;
const int Profile2Pin   = A3;
const int VoiceNotePin  = A4;
const int RecordPin     = A5;

//--------------------------------------------------------------------------------------------------

unsigned char image[1024];
Paint paint(image, 0, 0);    // width should be the multiple of 8 
Epd epd;
//unsigned long time_start_ms;
//unsigned long time_now_s;

//--------------------------------------------------------------------------------------------------

void setup() {
  
  Serial.begin(115200);
  if (epd.Init() != 0) {
      Serial.print("e-Paper init failed");
      return;
  }

  pinMode(HomePin, INPUT_PULLUP);
  pinMode(Profile1Pin, INPUT_PULLUP);
  pinMode(Tracking1Pin, INPUT_PULLUP);  
  pinMode(Focus1Pin, INPUT_PULLUP);
  pinMode(Profile2Pin, INPUT_PULLUP);
  pinMode(VoiceNotePin, INPUT_PULLUP);
  pinMode(RecordPin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(HomePin), Home, LOW);
  attachInterrupt(digitalPinToInterrupt(Profile1Pin), Profile1, LOW);
  attachInterrupt(digitalPinToInterrupt(Tracking1Pin), Tracking1, LOW);
  attachInterrupt(digitalPinToInterrupt(Focus1Pin), Focus1, LOW);
  attachInterrupt(digitalPinToInterrupt(Profile2Pin), Profile2, LOW);
  attachInterrupt(digitalPinToInterrupt(VoiceNotePin), VoiceNote, LOW);
  attachInterrupt(digitalPinToInterrupt(RecordPin), Record, LOW);

  
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(32);
  paint.SetHeight(200);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Little Time", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Buddy", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 30, 100, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(1000);

  if (epd.Init() != 0) {
      Serial.print("e-Paper init failed ");
      return;
     
  }

  epd.SetFrameMemory_Base(IMAGE_DATA);
  epd.DisplayFrame();

  //time_start_ms = millis();

}

//--------------------------------------------------------------------------------------------------

void loop() {


  
}
  
//--------------------------------------------------------------------------------------------------
//States//

void Home(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetWidth(32);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Home Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(180000);
}

void Profile1(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(32);
  paint.SetHeight(200);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Profile 1", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 30, 100, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(180000);
}


void Tracking1(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();  
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(32);
  paint.SetHeight(200);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Tracking 1", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 30, 100, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(180000);
}

void Focus1(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetWidth(32);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(12, 4, "Focus Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(180000);
}

void Profile2(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(32);
  paint.SetHeight(200);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Profile 2", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 30, 100, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(180000);
}

void VoiceNote(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetRotate(ROTATE_90);
  paint.SetWidth(32);
  paint.SetHeight(200);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Voice Note", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  
  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 30, 100, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(180000);
}

void Record(){
  epd.ClearFrameMemory(0xFF);   // bit set = white, bit reset = black
  epd.DisplayFrame();
  paint.SetWidth(32);
  paint.SetHeight(200);
  paint.SetRotate(ROTATE_90);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(10, 4, "Record Screen", &Font24, COLORED);
  epd.SetFrameMemory(paint.GetImage(), 50, 50, paint.GetWidth(), paint.GetHeight());
  epd.DisplayFrame();

  delay(180000);
}
