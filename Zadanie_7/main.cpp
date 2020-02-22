#include <iostream>
#include "Converter.h"
#include "FilesHelper.h"

int main() {
	Converter converter;
	//Loader loader;
//dsafadfadfadfasfa
	/*sdsadasdasdcafadsfasfac  sdfdafasfd
	dddsfdafadf*/
	std::vector<std::string> pathToFiles = FilesHelper::getPathToFilesFromDirectory("input");
//std::vector<std::string> pathToFiles = FilesHelper::getPathToFilesFromDirectory("input");
	for (auto it : pathToFiles) {
		std::cout << it << std::endl;

	}
	converter.separateAndSaveChannels(pathToFiles);
	//loader.getBlocksFromFile("1.bin");

	system("pause");

	/*for (auto it : pathToFiles) {
		std::cout << it << std::endl;

	}*/
	
}