#include <WiFi.h>
#include <HTTPClient.h>
#include <max6675.h>

int thermoDO = 19; int thermoCS = 23; int thermoCLK = 5;
MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);

const int heaterPin = 18;
float setpoint = 65.0;

String ssid = ""; String pass = "";

void setup() {
  Serial.begin(115200);
  pinMode(heaterPin, OUTPUT);
  Serial.println("Enter WiFi Credentials in Serial Monitor...");
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    // Basic Serial Input logic as used in previous projects
  }

  float t = thermocouple.readCelsius();
  if (t < setpoint) { digitalWrite(heaterPin, HIGH); } 
  else { digitalWrite(heaterPin, LOW); }

  HTTPClient http;
  http.begin("http://your-medtech-app.com/qa");
  http.addHeader("Content-Type", "application/json");
  String json = "{\"t\":" + String(t) + ",\"set\":" + String(setpoint) + "}";
  http.POST(json);
  http.end();
  
  delay(1000);
}
