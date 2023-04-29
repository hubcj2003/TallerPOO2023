#pragma once
#include "Bus.h"
#include "Carro.h"
#include "Bicicleta.h"
#include "Persona.h"
class Juego
{
private:
	Persona* persona;
	vector<Terrestre*> transportes;
	time_t tiempoInicial;
public:
	Juego(){
		persona = new Persona();
		tiempoInicial = time(0);
	}
	~Juego(){}
	void jugando() {
		char tecla;
		tecla = NULL;
		do
		{
			if (kbhit()) {
				tecla = getch();
				tecla = toupper(tecla);
			}
			persona->direccion(tecla);
			if (difftime(time(0), tiempoInicial) > 2.5) {
				agregarVeiculo();
				tiempoInicial = time(0);
			}
			eliminarVeiculos();
			logicaPersona();
			logicaVeiculos();
			_sleep(100);
		} while (colision());
		Console::Clear();
		cout << "Perdimos";
		getch();
	}
	void logicaPersona() {
		persona->borrar();
		persona->mover();
		persona->dibujar();
	}
	void logicaVeiculos() {
		for (int i = 0; i < transportes.size(); i++){
			transportes[i]->borrar();
			transportes[i]->mover();
			transportes[i]->dibujar();
		}
	}
	void agregarVeiculo() {
		switch (rand() % 3)
		{
		case 0:
			if(rand() % 2 == 0)
				transportes.push_back(new Bicicleta());
			break;
		case 1:transportes.push_back(new Carro()); break;
		case 2:transportes.push_back(new Bus()); break;
		}
	}
	void eliminarVeiculos() {
		for (int i = 0; i < transportes.size(); i++) {
			if (transportes[i]->getdx() == 0) {
				transportes[i]->borrar();
				transportes.erase(transportes.begin() + i);
			}
		}
	}
	bool colision() {
		for (int i = 0; i < transportes.size(); i++)
			if (transportes[i]->colision(persona->getx(), persona->gety(), persona->getancho(), persona->getalto()))
				if (transportes[i]->gettipo() != 1)
					return false; // terminar juego
		return true;
	}
};