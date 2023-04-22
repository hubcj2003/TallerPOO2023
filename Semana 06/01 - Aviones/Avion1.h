#pragma once
#include "Base.h"
class Avion1 : public Base
{
public:
	Avion1();
	~Avion1();
	void dibujar();
private:

};

Avion1::Avion1() : Base(11, 3)
{
}

Avion1::~Avion1()
{
}

void Avion1::dibujar() {
	Console::ForegroundColor = color;
	Console::SetCursorPosition(x, y);
	cout << "-----------";
	Console::SetCursorPosition(x, y + 1);
	cout << "_\\__(_)__/_";
	Console::SetCursorPosition(x, y + 2);
	cout << "   ./ \\.	";
	Console::ForegroundColor = ConsoleColor::Gray;
}