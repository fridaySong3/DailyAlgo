// https://www.acmicpc.net/problem/23309
#include <iostream>
#include <string>
#define MAX 1000000
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    int next[MAX + 1] = {
        0,
    };
    int prev[MAX + 1] = {
        0,
    };

    cin >> N >> M;
    int *init = new int[N];

    for (int i = 0; i < N; ++i)
    {
        cin >> init[i];
    }

    next[init[0]] = init[1];
    prev[init[0]] = init[N - 1];
    next[init[N - 1]] = init[0];
    prev[init[N - 1]] = init[N - 2];
    for (int i = 1; i < N - 1; ++i)
    {
        next[init[i]] = init[i + 1];
        prev[init[i]] = init[i - 1];
    }
    delete init;

    string cmd;
    int base, build;
    for (int i = 0; i < M; ++i)
    {
        cin >> cmd;
        if (cmd.compare("BN") == 0)
        {
            cin >> base >> build;
            if (next[build] != 0)
            {
                continue;
            }
            int neighbor = next[base];
            cout << neighbor << "\n";
            next[base] = build;
            prev[neighbor] = build;
            next[build] = neighbor;
            prev[build] = base;
        }
        else if (cmd.compare("BP") == 0)
        {
            cin >> base >> build;
            if (next[build] != 0)
            {
                continue;
            }
            int neighbor = prev[base];
            cout << neighbor << "\n";
            prev[base] = build;
            next[neighbor] = build;
            prev[build] = neighbor;
            next[build] = base;
        }
        else if (cmd.compare("CN") == 0)
        {
            cin >> base;
            int neighbor = next[base];
            cout << neighbor << "\n";
            next[base] = next[neighbor];
            prev[next[neighbor]] = base;
            next[neighbor] = 0;
            prev[neighbor] = 0;
        }
        else
        { // CP
            cin >> base;
            int neighbor = prev[base];
            cout << neighbor << "\n";
            prev[base] = prev[neighbor];
            next[prev[neighbor]] = base;
            next[neighbor] = 0;
            prev[neighbor] = 0;
        }
    }
    return 0;
}