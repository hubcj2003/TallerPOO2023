#pragma once
#include <iostream>
#include <string>
using namespace std;
using namespace System;
class Contrasenia
{
public:
	Contrasenia();
	Contrasenia(int plongitud);
	~Contrasenia();
	bool esSeguro();
	void generarContrasena();
	//METODOS DE ACCESO (getters setters)
	//GET -> RETORNAN UN VALOR (DEPENDEN DEL VALOR QUE RETORNAN)
	//SET -> MODIFICAN UN VALOR (SON VOID)
	void setLongitud(int nuevaLongitud);
	int getLongitud();
	string getContra();
private:
	int longitud;
	string contra;
};

Contrasenia::Contrasenia()
{
	longitud = 8; 
	contra = "";
}

Contrasenia::Contrasenia(int plongitud)
{
	longitud = plongitud;
	contra = "";
}

Contrasenia::~Contrasenia()
{
}

bool Contrasenia::esSeguro() {
	int cMay = 0, cMin = 0, cDig = 0;
	for (int i = 0; i < contra.size(); i++)
		if (contra[i] <= '9') cDig++;
		else if (contra[i] <= 'Z') cMay++;
		else cMin++;
	if (cMay > 2 && cMin > 1 && cDig > 5) return true;
	else return false;
}

void Contrasenia::generarContrasena() { //var = min + rand() % (max - min + 1)
	for (int i = 0; i < longitud; i++) {
		switch (rand() % 3) //0 1 2
		{		//"" += "1"   = "1"
		case 0: contra += to_string(rand()% 10); break; //NUMERO
			//"1" += "B"   = "1B"
		case 1: contra += char('A' + rand() % ('Z' - 'A' + 1)); break; //MAYUSCULA
			//"1B" += "z"   = "1Bz"
		case 2: contra += char('a' + rand() % ('z' - 'a' + 1)); break; //MINUSCULA
		}
	}
}

void Contrasenia::setLongitud(int nuevaLongitud) {
	longitud = nuevaLongitud;
}

int Contrasenia::getLongitud() {
	return longitud;
}

string Contrasenia::getContra() {
	return contra;
}