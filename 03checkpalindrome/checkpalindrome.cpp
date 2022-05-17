#include <iostream>
using namespace std;

bool solution(string inputString){
	string reverseInput = string(inputString.rbegin(), inputString.rend());
	return (inputString == reverseInput) ? true : false;
}
int main(void){
	cout << "Enter word to check if it is palindrome" << endl;
	string word;
	cin >> word;
	cout << solution(word);
	
	cout << "####################" << endl;

	string texto = "Erace una vez un barco chiquito" ;

	cout << "Texto : " << texto << endl;
	//cout << "Rbegin: " << texto.rbegin() << endl;
	//cout << "Rend  : " << texto.rend() << endl;

	return 0;
}
