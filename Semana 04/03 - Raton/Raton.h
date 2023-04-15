#pragma once
#include <iostream>
#define anchoConsola 120
#define altoConsola 30

using namespace std; 
using namespace System; 

class Raton
{
public:
	~Raton();
	Raton();
	Raton(int px, int py);
	void dibujar();
	void mover();
	void borrar();
private:
	int x, y, ancho, alto, dx, dy;
};

Raton::Raton()
{
	alto = 3;
	ancho = 19;

	x = rand() % (anchoConsola - ancho);
	y = rand() % (altoConsola - alto);

	dx = -1;
	dy = 1;
}

Raton::~Raton()
{
}

Raton::Raton(int px, int py) {
	alto = 3;
	ancho = 19;
	x = px;
	y = py;
	dx = -1;
	dy = 1;
}

void Raton::dibujar() {
	if (dx > 0) {
		Console::SetCursorPosition(x, y);
		cout << "       ____()()";
		Console::SetCursorPosition(x, y + 1);
		cout << "      /       @@";
		Console::SetCursorPosition(x, y + 2);
		cout << "`~~~~~\\_;m__m._ >o";
	}
	else {
		Console::SetCursorPosition(x, y);
		cout << "  ()()____";
		Console::SetCursorPosition(x, y + 1);
		cout << "@@        \\";
		Console::SetCursorPosition(x, y + 2);
		cout << "o < _.m__m;_/~~~~~`";
	}
}

void Raton::mover() { //EL DX VA TENER UN VALOR O POSITIVO O NEGATIVO
	if (x + dx < 0 || x + dx + ancho > anchoConsola) 
		dx = dx * -1;
	if (y + dy < 0 || y + dy + alto > altoConsola) 
		dy = dy * -1;
	x += dx;
	y += dy;
}

void Raton::borrar() {									  
	for (int i = 0; i < alto; i++)						  
		for (int j = 0; j < ancho; j++) {				  
			Console::SetCursorPosition(x + j, y+ i);	  
			cout << " ";
		}
}


