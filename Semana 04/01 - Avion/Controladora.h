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
	Avion1 * avion1;
	Avion2 * avion2;
	Avion3 * avion3;
	int op;
};

Controladora::Controladora()
{
	avion1 = new Avion1();
	avion2 = new Avion2();
	avion3 = new Avion3();
}

Controladora::~Controladora()
{
}

void Controladora::jugar() {
	cout << "Ingrese el avion que desea operar : ";
	cin >> op;
	Console::Clear();
	while (true)
	{
		switch (op)
		{
		case 1:
			avion1->borrar();
			avion1->mover();
			avion1->dibujar();
			break;
		case 2:
			avion2->borrar();
			avion2->mover();
			avion2->dibujar();
			break;
		case 3:
			avion3->borrar();
			avion3->mover();
			avion3->dibujar();
			break;
		}
		_sleep(100);
	}
}