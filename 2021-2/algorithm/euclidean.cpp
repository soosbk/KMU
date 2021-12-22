#include<iostream>

using namespace std;

unsigned int gcd(unsigned int a,unsigned int b){
	if(b==0) return a;
	else return gcd(b, a%b);
	
}

int main(){
	int case_num;
	unsigned int n1,n2;

	cin>>case_num;
	for(int i=0;i<case_num;i++){
		cin>>n1>>n2;
		
		if(n1<n2){
			unsigned int tmp=n1;
			n1=n2;
			n2=tmp;
		}

		cout<<gcd(n1,n2)<<endl;
		
	}
}
