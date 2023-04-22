#pragma once
#include <vector>
#include <conio.h>
#include "Alfa.h"
#include "Beta.h"
#include "Gamma.h"

class Jugar
{
public:
	Jugar();
	~Jugar();
	void jugar();
	void moverTodo();
	void dibujarTodo();
	void borrarTodo();
	void agregar();
private:
	vector<Nave*> naves;
	int cA, cB;
};

Jugar::Jugar()
{
	cA = cB = 0;
}

Jugar::~Jugar()
{
}

void Jugar::jugar(){
	char letra;
	string mensaje = "Comienza la invasión…!!!";
	Console::SetCursorPosition((anchoConsola - mensaje.size()) / 2, 15);
	cout << mensaje;
	_sleep(700);
	Console::Clear();
	do
	{
		letra = NULL;
		if (kbhit()) {
			letra = getch();
			letra = toupper(letra);
			if (letra == 'A')
				agregar();
		}
		borrarTodo();
		moverTodo();
		dibujarTodo();
		_sleep(100);
	} while (naves.size() < 10);
	Console::Clear();
	mensaje = "Hemos sido invadidos…!!!";
	Console::SetCursorPosition((anchoConsola - mensaje.size()) / 2, 15);
	cout << mensaje;
	getch();
}

void Jugar::agregar() {
	naves.push_back(new Alfa());
	cA++;
	if (cA == 2) {
		cA = 0;
		naves.push_back(new Beta());
		cB++;
	}
	if (cB == 2) {
		cB = 0;
		naves.push_back(new Gamma());
	}
}
void Jugar::moverTodo(){
	for (int i = 0; i < naves.size(); i++)
		naves[i]->mover();
}
void Jugar::dibujarTodo(){
	for (int i = 0; i < naves.size(); i++)
		naves[i]->dibujar();
}
void Jugar::borrarTodo(){
	for (int i = 0; i < naves.size(); i++)
		naves[i]->borrar();
}