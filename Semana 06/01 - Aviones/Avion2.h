#pragma once
#include "Base.h"
class Avion2 : public Base
{
public:
	Avion2();
	~Avion2();
	void dibujar();
private:

};

Avion2::Avion2() : Base(13, 3)
{
}

Avion2::~Avion2()
{
}

void Avion2::dibujar() {
	Console::ForegroundColor = color;

	Console::SetCursorPosition(x, y);
	cout << "    __!__";
	Console::SetCursorPosition(x, y + 1);
	cout << "-----<*>-----";
	Console::SetCursorPosition(x, y + 2);
	cout << "    o O o";
	Console::ForegroundColor = ConsoleColor::Gray;

}