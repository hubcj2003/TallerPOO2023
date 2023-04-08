#pragma once
#include "Eclipse.h"
#include <vector>
#include <string>

string datos[5] = {"America del Sur","Europa", "África", "America del Norte", "Asia"};

class Controlador
{
public:
	Controlador();
	~Controlador();
	void menu();
	void registrarDatos();
	void modificarDatos();
	void eliminarDatos();
	void mostrarDatos();
	void eclipsesEuropa();
	void eclipsesSismos();
	void eclipsesNoche();
private:
	vector<Eclipse*> eclipses;
};

Controlador::Controlador()
{

}

Controlador::~Controlador()
{
}

void Controlador::menu() {
	int op;
	do
	{
		cout << "1 - Registrar datos\n";
		cout << "2 - Modificar datos\n";
		cout << "3 - Eliminar datos\n";
		cout << "4 - Eclipses visibles en europa\n";
		cout << "5 - Eclipses con sismos\n";
		cout << "6 - Eclipses nocturnos\n";
		cout << "7 - Mostrar datos\n";
		cout << "0 - Salir\n";
		cout << "Ingrese la opcion : ";
		cin >> op;
		switch (op)
		{
		case 1: registrarDatos(); break;
		case 2: modificarDatos(); break;
		case 3: eliminarDatos(); break;
		case 4: eclipsesEuropa(); break;
		case 5: eclipsesSismos(); break;
		case 6: eclipsesNoche(); break;
		case 7:  mostrarDatos(); break;
		}
		system("pause");
		system("cls");
	} while (op != 0);
}

void Controlador::registrarDatos() {
	string tipo,  sismos, lluvias, visibilidad;
	Fecha * fecha;
	int dia, mes, anio, hora;
	cout << "Ingrese el tipo : ";
	cin >> tipo;
	cout << "Ingrese la fecha (dd mm aaaa): ";
	cin>> dia >> mes >> anio;
	fecha = new Fecha(dia, mes, anio);
	cout << "Ingrese la hora : ";
	cin >> hora;
	cout << "Ingrese sismos (si no) : ";
	cin >> sismos;
	cout << "Ingrese lluvias : ";
	cin >> lluvias;
	visibilidad = datos[rand() % 5];
	cout << "Ingrese la visibilidad : " << visibilidad;
	//getline(cin, visibilidad);
	Eclipse* eclipse = new Eclipse(tipo, fecha, hora, sismos, lluvias, visibilidad);
	eclipses.push_back(eclipse);
}

void Controlador::modificarDatos() {
	string tipo, sismos, lluvias, visibilidad;
	Fecha* fecha;
	int dia, mes, anio, hora;
	int indice;
	mostrarDatos();
	cout << "Ingrese dato a modificar : ";
	cin >> indice;
	cout << "Ingrese el tipo : ";
	cin >> tipo;
	cout << "Ingrese la fecha (dd mm aaaa): ";
	cin >> dia >> mes >> anio;
	fecha = new Fecha(dia, mes, anio);
	//cout << "Ingrese la hora : ";
	//cin >> hora;
	//cout << "Ingrese sismos (si no) : ";
	//cin >> sismos;
	//cout << "Ingrese lluvias : ";
	//cin >> lluvias;
	//visibilidad = datos[rand() % 5];
	//cout << "Ingrese la visibilidad : " << visibilidad;
	eclipses[indice]->settipo(tipo);
	eclipses[indice]->setfecha(fecha);
	//TERMINAR DE HACER LOS SETTERS
}
void Controlador::eliminarDatos() {
	int indice;
	mostrarDatos();
	cout << "Ingrese dato a eliminar : "; //3
	cin >> indice; //[][][][]
	eclipses.erase(eclipses.begin() + indice);
}
void Controlador::mostrarDatos() {
	for (int i = 0; i < eclipses.size(); i++)
		cout << i <<  " - " << eclipses[i]->getInfo();
}

void Controlador::eclipsesEuropa() {
	for (int i = 0; i < eclipses.size(); i++)
		if(eclipses[i]->getvisibilidad() == "Europa")
			cout << i << " - " << eclipses[i]->getInfo();
}
void Controlador::eclipsesSismos() {
	for (int i = 0; i < eclipses.size(); i++)
		if (eclipses[i]->getsismos() == "si")
			cout << i << " - " << eclipses[i]->getInfo();
}
void Controlador::eclipsesNoche() {
	for (int i = 0; i < eclipses.size(); i++)
		if (eclipses[i]->gethora() > 1800)
			cout << i << " - " << eclipses[i]->getInfo();
}