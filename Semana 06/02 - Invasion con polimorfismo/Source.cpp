#include "Jugar.h"

void main() {
	srand(time(0));
	Console::SetWindowSize(anchoConsola, altoConsola);
	Console::CursorVisible = false;
	Jugar* jugar = new Jugar();
	jugar->jugar();
}