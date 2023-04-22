#pragma once
#include <iostream>
#define anchoConsola 120
#define altoConsola 30

using namespace std;
using namespace System;

class Base
{
public:
	Base(int pancho, int palto);
	~Base();
	virtual void dibujar() = 0;
	void mover();
	void borrar();
protected: //Los atributos seran compartidos entre Padre e Hijas
	int x, y, ancho, alto, dx, dy;
	ConsoleColor color;
};

Base::Base(int pancho, int palto)
{
	ancho = pancho;
	alto = palto;
	x = rand() % (anchoConsola - ancho);
	y = rand() % (altoConsola - alto);
	dx = (rand() % 2 * 2 - 1) * 5; //-1 0 1
	dy = rand() % 3 - 1; // -1 0 1 
	color = ConsoleColor(rand() % 16);
}
Base::~Base()
{
}
void Base::mover() { 
	if (x + dx < 0 || x + dx + ancho > anchoConsola)
		dx = dx * -1;
	if (y + dy < 0 || y + dy + alto > altoConsola)
		dy = dy * -1;
	x += dx;
	y += dy;
}
void Base::borrar() {
	for (int i = 0; i < alto; i++)
		for (int j = 0; j < ancho; j++) {
			Console::SetCursorPosition(x + j, y + i);
			cout << " ";
		}
}