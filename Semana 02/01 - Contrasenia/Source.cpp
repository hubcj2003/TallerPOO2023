#include <iostream>
#include <vector>
#include "Contrasenia.h"

int main() {
	srand(time(0));
	int n = 5 + rand() % (10 - 5 + 1);
	vector<Contrasenia*> contras;//[][][]
	vector<bool> esSegura;
	for (int i = 0; i < n; i++) {
		Contrasenia* contra = new Contrasenia(18);
		contra->generarContrasena();
		contras.push_back(contra);
		esSegura.push_back(contra->esSeguro());
	}
	for (int i = 0; i < contras.size(); i++)
		cout << contras[i]->getContra()<< " " << esSegura[i] << endl;
	system("pause");
}