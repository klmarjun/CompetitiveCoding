#include <iostream>
using namespace std;

int main(){
    int max,min,num1,num2,num3;
    cin>>num1>>num2>>num3;
    if(num1>num2 && num1>num3){
        max = num1;
    }
    else{
        if(num2>num3){
            max=num2;
        }
        else{
            max=num3;
        }
    }
    
    if(num1<num2&&num1<num3){
        min=num1;
    }
    else{
        if(num2<num3){
            min=num2;
        }
        else{
            min=num3;
        }
    }
    
    cout<<max-min;
}