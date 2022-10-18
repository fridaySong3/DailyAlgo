// https://www.acmicpc.net/problem/1786
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void preprocessing(const string& P, vector<int>& pi) {
    int m = 0;
    for (int i=1; i<P.length(); ++i) {
        while (m > 0 && P[i] != P[m]) {
            m = pi[m-1];
        }
        if (P[i] == P[m]) {
            pi[i] = ++m;
        }
    }
}

void KMP(const string& T, const string& P, vector<int>& loc) {
    vector<int> pi(P.length(), 0);
    preprocessing(P, pi);

    int m = 0;
    for (int i=0; i<T.length(); ++i) {
        while (m > 0 && T[i] != P[m]) {
            m = pi[m-1];
        }
        if (T[i] == P[m]) {
            ++m;
            if (m == P.length()) {
                loc.push_back( i-m+1 );
                m = pi[m-1];
            }
        }
    }
}

int main() {
	ios::sync_with_stdio(false); 
	cin.tie(NULL);
    
    string T, P;
    getline(cin, T);
    getline(cin, P);
    vector<int> loc;

    KMP(T, P, loc);

    cout << loc.size() << endl;
    for (const int& l : loc) {
        cout << l+1 << " ";
    }
    cout << endl;

	return 0;
}