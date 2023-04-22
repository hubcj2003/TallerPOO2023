#pragma once
#include "Nave.h"
class Beta : public Nave
{
public:
	Beta();
	~Beta();
private:

};

Beta::Beta() : Nave(50, 11, 3)
{
	figura.push_back("   .-- - .");
	figura.push_back("_ / __~0_\\_");
	figura.push_back("(_________)");
}

Beta::~Beta()
{
}