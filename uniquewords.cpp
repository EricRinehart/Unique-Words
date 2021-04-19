#include <iostream> //IO
#include <fstream> //Read a file
#include <string> //Using strings
#include <set> //Set collection
#include <algorithm> //Iterate with for_each
using namespace std; //This program does not need inline 'std::'

int main() {
	set<string> unique; //Empty set for unique words
	string word; //Empty string for words
	string filename; //Empty string for user input
	

	cout << "which file do you want to open?";
	cin >> filename; //Input file to read

	ifstream read(filename.c_str()); //Assign input as readable file

	//Open read,
	if (read.is_open()) {
		//Extract each word from the file
		while (read >> word) {
			//Convert word to lowercase word
			for_each(word.begin(), word.end(), [](char &c) {
				c = ::tolower(c);
			});
			//Iterate over characters in string to identify punctuation
			//Remove punctuation
			for (int i = 0, len = word.size(); i < len; i++) {
				if (ispunct(word[i])) {
					word.erase(i--, 1);
					len = word.size();
				}
			}
			unique.insert(word); //Insert word into set
		}
		read.close(); //Close read file
	}
	else cout << "Unable to open file\n"; //Error message if input incorrect or file not found

	//Display the elements of the set
	for (auto it = unique.begin(); it != unique.end(); it++)
		cout << *it << "\n";

	return 0; //Close program

	
}