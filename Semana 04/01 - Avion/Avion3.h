#pragma once
#include "Base.h"
class Avion3 : public Base
{
public:
	Avion3();
	~Avion3();
	void dibujar();
private:

};

Avion3::Avion3() : Base(7, 2)
{
}

Avion3::~Avion3()
{
}

void Avion3::dibujar() {
	Console::ForegroundColor = color;
	Console::SetCursorPosition(x, y);
	cout << "   |";
	Console::SetCursorPosition(x, y + 1);
	cout << "--=O=--";
	Console::ForegroundColor = ConsoleColor::Gray;

}