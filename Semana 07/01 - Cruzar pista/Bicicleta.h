#pragma once
#include "Terrestre.h"
class Bicicleta : public Terrestre
{
public:
	Bicicleta() {
		tipo = 1;
		dy = 0;
		ancho = 6;
		alto = 2;
		y = rand() % (altoConsola - alto + 1);
		x = rand() % (anchoConsola - ancho + 1);
		dx = rand() % 2 * 2 - 1;
	}
	~Bicicleta() {}
	void mover() {
		movimineto(-dx, 0,1, 1);
	}
	void dibujar() {
		if (dx < 0) {
			Console::SetCursorPosition(x, y);
			cout << "/_..";
			Console::SetCursorPosition(x, y + 1);
			cout << "(o)(o)";
		}
		else {
			Console::SetCursorPosition(x, y);
			cout << ".._\\";
			Console::SetCursorPosition(x, y + 1);
			cout << "(o)(o)";
		}
	}
};