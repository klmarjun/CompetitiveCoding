#include <bits/stdc++.h>
using namespace std;

int main() {
	int iter,x,y;
	cin>>iter;
	for(int i=0;i<iter;i++){
	    cin>>x>>y;
	    
	    if(x+(x*0.07)<y){
	        cout<<"NO"<<endl;
	    }
	    else{
	        cout<<"YES"<<endl;
	    }
	}

}
