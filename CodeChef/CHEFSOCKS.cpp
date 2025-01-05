#include <bits/stdc++.h>
using namespace std;

int main() {
	int amt_req,chef_money,chef_got;
	cin>>amt_req>>chef_money>>chef_got;
	if(amt_req>chef_money+chef_got){
	    cout<<"NO";
	}
	else{
	    cout<<"YES";
	}
}
