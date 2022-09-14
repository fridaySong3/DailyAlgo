// https://www.acmicpc.net/problem/13334
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <utility>

#define NUM 100000

using namespace std;

int main()
{
    int N, D;
    pair<int, int> lines[NUM];
    
    cin >> N;
    for (int i=0; i<N; ++i) {
        int a, b;
        cin >> a >> b;
        if (a < b) {
            lines[i].first = a;
            lines[i].second = b;
        } else {
            lines[i].first = b;
            lines[i].second = a;
        }
    }
    cin >> D;
    
    sort(lines, lines+N);
    
    int ans = 0;
    priority_queue<int> pq;
    for (int i=N-1; i>=0; --i) {
        pq.push(lines[i].second);
        int end = lines[i].first + D;
        while (!pq.empty() && end < pq.top()) {
            pq.pop();
        }
        ans = max(ans, int(pq.size()));
    }
    cout << ans;
    return 0;
}
