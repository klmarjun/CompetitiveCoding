#include <bits/stdc++.h>
using namespace std;

int main() {
	int iter,a,b,c,x;
	cin>>iter;
	for(int i=0;i<iter;i++){
	    cin>>a>>b>>c>>x;
	    if(a+b>=x||b+c>=x||c+a>=x){
	        cout<<"YES"<<endl;
	    }
	    else{
	        cout<<"NO"<<endl;
	    }
	}
}
