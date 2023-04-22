#pragma once
#include <iostream>
#define anchoConsola 120
#define altoConsola 30

using namespace std;
using namespace System;

class Nave
{
public:
	Nave(int px, int pancho, int palto);
	~Nave();
	virtual void dibujar() = 0;
	void mover();
	void borrar();
protected:
	int x, y, dx, dy, ancho, alto;
};

Nave::Nave(int px, int pancho, int palto)
{
	ancho = pancho;
	alto = palto;
	x = px;
	y = 0;
	dx = 0;
	dy = 1;
}

Nave::~Nave()
{
}
void Nave::mover() {
	if (x + dx < 0 || x + dx + ancho > anchoConsola) dx *= -1;
	if (y + dy < 0 || y + dy + alto > altoConsola) dy *= -1;
	x += dx;
	y += dy;
}
void Nave::borrar() {
	for (int i = 0; i < alto; i++)
		for (int j = 0; j < ancho; j++) {
			Console::SetCursorPosition(x + j, y + i);
			cout << " ";
		}
}