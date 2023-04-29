#pragma once
#include "Terrestre.h"
class Bus : public Terrestre
{
public:
	Bus() {
		tipo = 3;
		ascii.push_back("   __________ ");
		ascii.push_back(" _/_|[][][][]|");
		ascii.push_back("(|           |");
		ascii.push_back(" =--OO----OO-=");
		dy = 0;
		ancho = 14;
		alto = 4;
		y = rand() % (altoConsola - alto + 1);
		x = anchoConsola - ancho;
		dx = -1;
	}
	~Bus() {}
	void mover() {
		movimineto(0, 0, 3 + rand() % 4, 1);
	}
};