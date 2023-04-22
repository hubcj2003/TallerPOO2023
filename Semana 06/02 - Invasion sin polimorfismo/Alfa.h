#pragma once
#include "Nave.h"
class Alfa : public Nave
{
public:
	Alfa();
	~Alfa();
	void dibujar();
private:

};

Alfa::Alfa() : Nave(4, 19, 5)
{
}

Alfa::~Alfa()
{
}

void Alfa::dibujar()
{
	Console::SetCursorPosition(x, y);
	cout << "     _.-- - ._";
	Console::SetCursorPosition(x, y + 1);
	cout << "    .'       '.";
	Console::SetCursorPosition(x, y + 2);
	cout << "_.-~======== = ~-._";
	Console::SetCursorPosition(x, y + 3);
	cout << " (_______________)";
	Console::SetCursorPosition(x, y + 4);
	cout << "    \_______ /";	
}