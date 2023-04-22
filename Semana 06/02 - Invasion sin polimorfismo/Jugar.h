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
	vector<Alfa*> alfas;
	vector<Beta*> betas;
	vector<Gamma*> gammas;
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
	} while (alfas.size() + betas.size() + gammas.size() < 10);
	Console::Clear();
	mensaje = "Hemos sido invadidos…!!!";
	Console::SetCursorPosition((anchoConsola - mensaje.size()) / 2, 15);
	cout << mensaje;
	getch();
}

void Jugar::agregar() {
	alfas.push_back(new Alfa());
	cA++;
	if (cA == 2) {
		cA = 0;
		betas.push_back(new Beta());
		cB++;
	}
	if (cB == 2) {
		cB = 0;
		gammas.push_back(new Gamma());
	}
}
void Jugar::moverTodo(){
	for (int i = 0; i < alfas.size(); i++)
		alfas[i]->mover();
	for (int i = 0; i < betas.size(); i++)
		betas[i]->mover();
	for (int i = 0; i < gammas.size(); i++)
		gammas[i]->mover();
}
void Jugar::dibujarTodo(){
	for (int i = 0; i < alfas.size(); i++)
		alfas[i]->dibujar();
	for (int i = 0; i < betas.size(); i++)
		betas[i]->dibujar();
	for (int i = 0; i < gammas.size(); i++)
		gammas[i]->dibujar();
}
void Jugar::borrarTodo(){
	for (int i = 0; i < alfas.size(); i++)
		alfas[i]->borrar();
	for (int i = 0; i < betas.size(); i++)
		betas[i]->borrar();
	for (int i = 0; i < gammas.size(); i++)
		gammas[i]->borrar(); 
	//for each (Alfa * a in alfas)
	//	a->borrar();
	//for(Alfa* a : alfas)
	//	a->borrar();
}