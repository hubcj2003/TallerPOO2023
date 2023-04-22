#pragma once
#include "Avion1.h"
#include "Avion2.h"
#include "Avion3.h"

class Controladora
{
public:
	Controladora();
	~Controladora();
	void jugar();
private:
	Base * avion;
	int op;
};

Controladora::Controladora()
{
}

Controladora::~Controladora()
{
}

void Controladora::jugar() {
	cout << "Ingrese el avion que desea operar : ";
	cin >> op;
	Console::Clear();
	switch (op)
	{
	case 1: avion = new Avion1(); break;
	case 2: avion = new Avion2(); break;
	case 3: avion = new Avion3(); break;
	}
	while (true)
	{
		avion->borrar();
		avion->mover();
		avion->dibujar();
		_sleep(100);
	}
}