#pragma once
#include "Terrestre.h"
class Carro : public Terrestre
{
public:
	Carro(){
		tipo = 2;
		ascii.push_back("  | ~\\_");
		ascii.push_back("[| _ |-");
		ascii.push_back("(_)(_)");
		dy = 0;
		ancho = 7;
		alto = 3;
		y = rand() % (altoConsola - alto + 1);
		x = 0;
		dx = 1;
	}
	~Carro(){}
	void mover() {
		movimineto(0, 0, 1 + rand() % 4, 1);
	}
};