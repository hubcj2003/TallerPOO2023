#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <conio.h>
#define anchoConsola 100
#define altoConsola 30
#define izquierda 75
#define derecha 77
#define arriba 72
#define abajo 80
using namespace std;
using namespace System;
class Terrestre
{
protected:
	int x, y, ancho, alto, dx, dy, tipo;
	vector<string> ascii;
public:
	Terrestre() {
	}
	~Terrestre(){}
	void movimineto(int pdx, int pdy, int vX, int vY){
		int auxdx = dx * vX;
		int auxdy = dy * vY;
		if (x + auxdx < 0 || x + auxdx + ancho > anchoConsola) {
			dx = pdx;
			auxdx = dx * vX;
		}
		if (y + auxdy < 0 || y + auxdy + alto > altoConsola) {
			dy = pdy;
			auxdy = dy * vY;
		}
		x += auxdx;
		y += auxdy;
	}
	void borrar(){
		for (int i = 0; i < alto; i++)
			for (int j = 0; j < ancho; j++) {
				Console::SetCursorPosition(x + j, y + i);
				cout << " ";
			}
	}
	virtual void dibujar(){
		for (int i = 0; i < ascii.size(); i++) {
			Console::SetCursorPosition(x, y + i);
			cout << ascii[i];
		}
	}
	bool colision(int ex, int ey, int eancho, int ealto) {
		return x < ex + eancho && ex < x + ancho &&
				y < ey + ealto && ey < y + alto;
	}
	virtual void mover(){}
	int getx    (){return x    ;} 
	int gety    (){return y    ;} 
	int getancho(){return ancho;}
	int getalto (){return alto ;} 
	int getdx   (){return dx   ;} 
	int getdy   (){return dy   ;} 
	int gettipo (){return tipo ;}
	void setx    (int valor){x     = valor;} 
	void sety    (int valor){y     = valor;} 
	void setancho(int valor){ancho = valor;}
	void setalto (int valor){alto  = valor;} 
	void setdx   (int valor){dx    = valor;} 
	void setdy   (int valor){dy    = valor;} 
	void settipo (int valor){tipo  = valor;}
};