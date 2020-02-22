#include <iostream>
#include  
#include  

int main() {
	Converter converter;
	 
 
	 
	std::vector<std::string> pathToFiles = FilesHelper::getPathToFilesFromDirectory( );
 
	for (auto it : pathToFiles) {
		std::cout << it << std::endl;

	}
	converter.separateAndSaveChannels(pathToFiles);
	 

	system( );

	 
	
}