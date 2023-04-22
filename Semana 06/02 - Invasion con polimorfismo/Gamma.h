#pragma once
#include "Nave.h"
class Gamma : public Nave
{
public:
	Gamma();
	~Gamma();
private:

};

Gamma::Gamma() : Nave(100, 18, 10)
{
	figura.push_back("        .");
	figura.push_back("        |");
	figura.push_back("     .-\"^\"-.");
	figura.push_back("   / _....._ \\");
	figura.push_back("   . - \"` `\" -. ");
	figura.push_back("   (ooo ooo ooo)  ");
	figura.push_back(" '-.,_________,.-'");
	figura.push_back("        / \\");
	figura.push_back("     _ /   \\_");
	figura.push_back("     `\"`    `\"`");
}

Gamma::~Gamma()
{
}