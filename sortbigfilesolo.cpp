#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <ctime>	
using namespace std;
int main() {
	int m, n;
	n = 1000; m = 100;
	ofstream io("input.txt");//открываю на запись файл input.txt
	ifstream ip("input.txt");
	srand(unsigned(time(0))); //записываю туда n рандомных чисел от 0 до 10^9
	for (int i = 1; i <= n; i++) {
		io << rand() % 1000000000 << endl;
	}
	vector<ofstream> gg(n / m); //создаю вектор из потоков на запись
	int x, y, l;
	x = 1; y = m;
	for (int i = 0; i < n / m; i++) {
		vector<int> a;
		gg.push_back(ofstream("f" + to_string(i) + ".txt"));//добавл€ю в вектор потоков файл каждый раз, когда в исходном файле проходит m строчек
		ofstream out("f" + to_string(i) + ".txt");
		ifstream in("f" + to_string(i) + ".txt");
		for (int j = x; j <= y; j++) {
			ip >> l;
			a.push_back(l);// добавл€ю в вектор а числа (всего m) из исходного файла
		}
		sort(a.begin(), a.end()); //сортирую все добавленные в i-й файл числа
		for (int z = 0; z < size(a); z++) {
			out << a[z] << endl; //добавл€ю в каждый файл отсортированный вектор  из m чисел
		}
		out.close();
		in.close(); // закрываю i-й файл
		x = y; y = y + m;
	}
	io.close();
	ip.close(); //закрываю исходный файл
	int b;
	vector<int> s(n / m);
	vector<ifstream> ggg(n / m); // создаю вектор потоков на считывание 
	for (int i = 0; i < n / m; i++) {
		ggg[i].open("f" + to_string(i) + ".txt"); // открываю все наши n/m файлов на считывание 
		ggg[i] >> b; // добавл€ю в вектор s самое первое число из каждого файла 
		s[i] = b;
	}
	ofstream pot("output.txt"); // открываю выходной файл output.txt
	int min, ind, el;
	min = 999999999;
	while (size(s) != 0) {
		for (int i = 0; i < size(s); i++) {
			if (s[i] < min) { // ищу минимум в векторе из чисел вз€тых из файлов
				min = s[i];
				ind = i; // запоминаю индекс минимума
			}
		}
		pot << min << endl; //добавл€ю минимум в выходной файл
		min = 999999999;
		if (ggg[ind] >> el) { //считываю из ind-го файла следующий элемент и присваиваю значение в векторе чисел на ind-й индекс слеующего элемента из ind-го файла
			s[ind] = el;
		}
		else { //если нет элемента, то удал€ю элемент на ind-м месте в векторах с числами и входными потоками
			ggg[ind].close(); // закрываю каждый файл
			s.erase(s.begin() + ind);
			ggg.erase(ggg.begin() + ind);
		}
	}
	pot.close(); // закрываю входной файл
	system("pause");
	return 0;
}