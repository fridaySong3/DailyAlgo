// https://www.acmicpc.net/problem/15658
#include <iostream>
#include <algorithm>
#include <numeric>

#define MAX_N 11
#define OP_NUM 4

using namespace std;

typedef long long int ll;

int N;
int arr[MAX_N];
int op[OP_NUM], rest[OP_NUM], chosen[OP_NUM];
ll big = -(10e10), small = 10e10;

ll add(ll a, ll b) {
    return a + b;
}

ll sub(ll a, ll b) {
    return a - b;
}

ll mul(ll a, ll b) {
    return a * b;
}

ll divi(ll a, ll b) {
    return a / b;
}

ll (*f[OP_NUM])(ll, ll) = {add, sub, mul, divi};

void arrange(int n, int step, ll rst) {
    if (step == N) {
        big = max(big, rst);
        small = min(small, rst);
        return;
    }
    for (int i=0; i<=n; ++i) {
        if (chosen[i] > 0) {
            chosen[i] -= 1;
            arrange(n, step+1, f[i](rst, arr[step]));
            chosen[i] += 1;
        }
    }
}

void choose(int f, int n) {
    int beg = f - rest[n];
    if (op[n] < beg) {
        return;
    }
    int end = min(op[n], f);
    for (int j=beg; j<=end; ++j) {
        chosen[n] = j;
        int new_f = f - j;
        if (new_f == 0) {
            arrange(n, 1, arr[0]);
        } else {
            choose(new_f, n+1);
        }
    }
}

int main()
{
    cin >> N;
    for (int i=0; i<N; ++i) {
        cin >> arr[i];
    }
    for (int i=0; i<OP_NUM; ++i) {
        cin >> op[i];
    }
    for (int i=0; i<OP_NUM; ++i) {
        rest[i] = accumulate(op+(i+1), op+OP_NUM, 0);
    }
    
    choose(N-1, 0);
    
    cout << big << "\n" << small;
    return 0;
}