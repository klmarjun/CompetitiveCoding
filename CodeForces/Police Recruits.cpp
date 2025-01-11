#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> events(n);
    
    for (int i = 0; i < n; i++) {
        cin >> events[i];
    }

    int untreated_crimes = 0, available_officers = 0;

    for (int event : events) {
        if (event == -1) {
            if (available_officers > 0) {
                available_officers--;
            } else {
                untreated_crimes++;
            }
        } else {
            available_officers += event;
        }
    }

    cout << untreated_crimes;
    return 0;
}
