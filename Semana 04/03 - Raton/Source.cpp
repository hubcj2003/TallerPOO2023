#include <conio.h>
#include <vector>
#include "Raton.h"

void main() {
	Console::SetWindowSize(anchoConsola, altoConsola);
	Console::CursorVisible = false;
	srand(time(0));
	vector<Raton*> ratones;
	int n = 3 + rand() % 5;
	for (int i = 0; i < n; i++)
		ratones.push_back(new Raton());
	char tecla = NULL;
	do
	{
		for (int i = 0; i < ratones.size(); i++){
			ratones[i]->borrar();
			ratones[i]->mover();
			ratones[i]->dibujar();
		}
		if (kbhit()) {
			tecla = getch();
			tecla = toupper(tecla);
		}
		_sleep(100);
	} while (tecla != 'X');
}