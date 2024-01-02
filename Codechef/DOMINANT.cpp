#include <bits/stdc++.h>
using namespace std;

int main() {
	int iter,x,y,z;
	cin>>iter;
	for(int i=0;i<iter;i++){
	    cin>>x>>y>>z;
	    if(x>y+z || y>z+x || z>y+x){
	        cout<<"YES"<<endl;
	    }
	    else{
	        cout<<"NO"<<endl;
	    }
	}

}
