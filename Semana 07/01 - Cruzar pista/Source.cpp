#include "Juego.h"

void main() {
	srand(time(0));
	Console::SetWindowSize(anchoConsola, altoConsola);
	Console::CursorVisible = false;
	Juego* juego = new Juego();
	juego->jugando();
}