#pragma once
#include "Nave.h"
class Alfa : public Nave
{
public:
	Alfa();
	~Alfa();
private:

};

Alfa::Alfa() : Nave(4, 19, 5)
{
	figura.push_back("     _.-- - ._");
	figura.push_back("    .'       '.");
	figura.push_back("_.-~======== = ~-._");
	figura.push_back(" (_______________)");
	figura.push_back("    \_______ /");
}

Alfa::~Alfa()
{
}