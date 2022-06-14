// https://www.acmicpc.net/problem/1213
#include <iostream>
#include <algorithm>

#define MAX 50+1
#define ALPHA_NUM 26+1

using namespace std;

int main() {
	int dict[ALPHA_NUM] = {0,};
	char name[MAX];
	cin >> name;
	
	for(int i=0; name[i]!='\0'; ++i) {
		int d = name[i] - 'A';
		++dict[d];
	}
	
	bool odd_exist = false;
	int odd_idx = 0;
	char palin[MAX];
	int p_len = 0;
	for(int i=0; i<ALPHA_NUM; ++i) {
		if(dict[i] % 2 != 0) { // if odd
			if(odd_exist == false) {
				odd_exist = true;
				odd_idx = i;
			}
			else {
				cout << "I'm Sorry Hansoo\n";
				return 0;
			}
		}
		for(int j=0; j<dict[i]/2; ++j) {
			palin[p_len++] = char('A' + i);
		}
	}
	palin[p_len++] = '\0';
	
	cout << palin;
	if(odd_exist) {
		cout << char('A' + odd_idx);
	}
	reverse(palin, palin+p_len-1);
	cout << palin << endl;
	
	return 0;
}
