
// pins for the encoder inputs

String test;

// ===== Initializations ==========

double B1A = 330.0;
double B3A = 330.0;
double B1B = 330.0;
double B3B = 330.0;

double B2B = 330.0;
double B4B = 330.0; 
double B2A = 330.0;
double B4A = 330.0;

double PSARJ = 30.0;
double SSARJ = 0.0;
double PTRRJ = -10.0; // TRRJ's expect +/- 180 deg commands (limited to +/- 135-ish on ISS).  Requires custom scaling later.
double STRRJ = 0.0;
boolean AOS = false;

int MimiAllServoVals=0;

int servonum_B1A = 0;
int servonum_B3A = 1;
int servonum_B1B = 2;
int servonum_B3B = 3;

int servonum_B2B = 4;
int servonum_B4B = 5;
int servonum_B2A = 6;
int servonum_B4A = 7;

int servonum_PSARJ = 8;
int servonum_SSARJ = 9;
int servonum_PTRRJ = 10;
int servonum_STRRJ = 11;




int pulselen_B1A = 0;
int pulselen_B3A = 0;
int pulselen_B1B = 0;
int pulselen_B3B = 0;

int pulselen_B2B = 0;
int pulselen_B4B = 0;
int pulselen_B2A = 0;
int pulselen_B4A = 0;

int pulselen_PSARJ = 0;
int pulselen_SSARJ = 0;
int pulselen_PTRRJ = 0;
int pulselen_STRRJ = 0;
