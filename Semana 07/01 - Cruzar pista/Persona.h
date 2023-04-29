#pragma once
#include "Terrestre.h"
class Persona : public Terrestre
{
public:
	Persona() {
		dy = dx = 0;
		ancho = alto = 1;
		y = altoConsola - alto - 2;
		x = rand() % (anchoConsola - ancho + 1);
	}
	~Persona() {}
	void mover() {
		movimineto(0, 0, 2, 1);
	}
	void direccion(char tecla) {
		dx = dy = 0;
		switch (tecla)
		{
		case arriba: dy = -1; break;
		case abajo: dy = 1; break;
		case izquierda: dx = -1; break;
		case derecha:dx = 1; break;
		}
	}
	void dibujar() {
		Console::SetCursorPosition(x, y);
		cout << char(254);
	}
};