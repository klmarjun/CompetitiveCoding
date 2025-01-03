#include <bits/stdc++.h>
using namespace std;

int main() {
    int amt,disc;
    cin>>amt>>disc;
    if(amt>=disc){
        cout<<amt-disc;
    }
    else{
        cout<<0;
    }
}