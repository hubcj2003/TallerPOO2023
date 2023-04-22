#include "Jugar.h"

void main() {
	Console::SetWindowSize(anchoConsola, altoConsola);
	Console::CursorVisible = false;
	Jugar* jugar = new Jugar();
	jugar->jugar();
}