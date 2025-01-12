#include <iostream>
using namespace std;

int maxProblemsSolved(int n, int k) {
    int available_time = 240 - k;
    int time_spent = 0;
    int solved_problems = 0;

    for (int i = 1; i <= n; ++i) {
        time_spent += 5 * i;
        if (time_spent > available_time) {
            break;
        }
        ++solved_problems;
    }

    return solved_problems;
}

int main() {
    int n, k;
    cin >> n >> k;

    cout << maxProblemsSolved(n, k) << endl;

    return 0;
}
