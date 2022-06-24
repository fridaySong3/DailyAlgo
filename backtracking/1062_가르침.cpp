#include <bits/stdc++.h>

#define max(x, y) (((x) > (y)) ? (x) : (y))

using namespace std;

int N, K;
unsigned int* words;

unsigned int to_bit(const string& s) {
	unsigned int bit = 0;
	for(int i=0; i<s.size(); ++i) {
		bit |= 1 << (s[i] - 'a');
	}
	return bit;
}

int count_readable(unsigned int teach) {
	int cnt = 0;
	for(int i=0; i<N; ++i) {
		if ((words[i] & teach) == words[i]) {
			++cnt;
		}
	}
	return cnt;
}

int dfs(int left_K, int start, unsigned int teach) {
	if (left_K == 0) {
		return count_readable(teach);	
	}
	int max_cnt = -1;
	for(int i=start; i<26; ++i) {
		unsigned int alpha = 1 << i;
		
		if ((teach & alpha) == 0) {
			int cnt = dfs(left_K-1, i+1, teach|alpha);
			max_cnt = max(max_cnt, cnt);
		}
	}
	return max_cnt;
}

int main() {
//	ios::sync_with_stdio(false); 
//	cin.tie(NULL);
	
	cin >> N >> K;
	words = new unsigned int[N];
	for(int i=0; i<N; ++i) {
		string s;
		cin >> s;
		words[i] = to_bit(s);
	}
	if (K < 5) {
		delete words;
		cout << 0;
		return 0;
	}
	
	unsigned int teach = to_bit("antic");
	
	int answer = dfs(K-5, 0, teach);
	cout << answer;
	delete words;
	return 0;
}
