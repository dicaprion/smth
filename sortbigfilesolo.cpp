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
	ofstream io("input.txt");//�������� �� ������ ���� input.txt
	ifstream ip("input.txt");
	srand(unsigned(time(0))); //��������� ���� n ��������� ����� �� 0 �� 10^9
	for (int i = 1; i <= n; i++) {
		io << rand() % 1000000000 << endl;
	}
	vector<ofstream> gg(n / m); //������ ������ �� ������� �� ������
	int x, y, l;
	x = 1; y = m;
	for (int i = 0; i < n / m; i++) {
		vector<int> a;
		gg.push_back(ofstream("f" + to_string(i) + ".txt"));//�������� � ������ ������� ���� ������ ���, ����� � �������� ����� �������� m �������
		ofstream out("f" + to_string(i) + ".txt");
		ifstream in("f" + to_string(i) + ".txt");
		for (int j = x; j <= y; j++) {
			ip >> l;
			a.push_back(l);// �������� � ������ � ����� (����� m) �� ��������� �����
		}
		sort(a.begin(), a.end()); //�������� ��� ����������� � i-� ���� �����
		for (int z = 0; z < size(a); z++) {
			out << a[z] << endl; //�������� � ������ ���� ��������������� ������  �� m �����
		}
		out.close();
		in.close(); // �������� i-� ����
		x = y; y = y + m;
	}
	io.close();
	ip.close(); //�������� �������� ����
	int b;
	vector<int> s(n / m);
	vector<ifstream> ggg(n / m); // ������ ������ ������� �� ���������� 
	for (int i = 0; i < n / m; i++) {
		ggg[i].open("f" + to_string(i) + ".txt"); // �������� ��� ���� n/m ������ �� ���������� 
		ggg[i] >> b; // �������� � ������ s ����� ������ ����� �� ������� ����� 
		s[i] = b;
	}
	ofstream pot("output.txt"); // �������� �������� ���� output.txt
	int min, ind, el;
	min = 999999999;
	while (size(s) != 0) {
		for (int i = 0; i < size(s); i++) {
			if (s[i] < min) { // ��� ������� � ������� �� ����� ������ �� ������
				min = s[i];
				ind = i; // ��������� ������ ��������
			}
		}
		pot << min << endl; //�������� ������� � �������� ����
		min = 999999999;
		if (ggg[ind] >> el) { //�������� �� ind-�� ����� ��������� ������� � ���������� �������� � ������� ����� �� ind-� ������ ��������� �������� �� ind-�� �����
			s[ind] = el;
		}
		else { //���� ��� ��������, �� ������ ������� �� ind-� ����� � �������� � ������� � �������� ��������
			ggg[ind].close(); // �������� ������ ����
			s.erase(s.begin() + ind);
			ggg.erase(ggg.begin() + ind);
		}
	}
	pot.close(); // �������� ������� ����
	system("pause");
	return 0;
}