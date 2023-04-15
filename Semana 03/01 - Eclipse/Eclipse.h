#pragma once
#include <iostream>
#include "Fecha.h"

using namespace std;

class Eclipse
{
public:
	Eclipse(string ptipo,Fecha* pfecha, int phora, string psismos, string plluvias, string pvisibilidad);
	~Eclipse();
	string getInfo();
	void settipo(string valor);
	void setfecha(Fecha * valor);
	void sethora(int valor);
	void setsismos(string valor);
	void setlluvias(string valor);
	void setvisibilidad(string valor);
	int gethora();
	string getsismos();
	string getvisibilidad();
private:
	string tipo;
	Fecha * fecha;
	int hora;
	string sismos, lluvias, visibilidad;
};

Eclipse::Eclipse(string ptipo, Fecha* pfecha, int phora, string psismos, string plluvias, string pvisibilidad)
{
	tipo = ptipo;
	fecha = pfecha;
	hora = phora;
	sismos = psismos;
	lluvias = plluvias;
	visibilidad = pvisibilidad;
}

Eclipse::~Eclipse()
{
}

string Eclipse::getInfo() {
	return tipo + "\t" + fecha->getFecha() + "\t" + to_string(hora) + "\t" + sismos + "\t" + lluvias + "\t" + visibilidad + "\n";
}

void  Eclipse::settipo		 (string valor) {tipo		= valor;  }
void  Eclipse::setfecha		 (Fecha* valor) {fecha		= valor;  }
void  Eclipse::sethora		 (int valor)    {hora		= valor;  }
void  Eclipse::setsismos     (string valor) {sismos     = valor; }
void  Eclipse::setlluvias    (string valor) {lluvias    = valor; }
void  Eclipse::setvisibilidad(string valor) {visibilidad= valor; }

int    Eclipse::gethora() { return hora; }
string Eclipse::getsismos() { return sismos; }
string Eclipse::getvisibilidad() { return visibilidad; }