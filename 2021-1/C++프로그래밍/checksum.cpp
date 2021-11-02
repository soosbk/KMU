#include<iostream>
using namespace std;

int main(){
	unsigned int num=0x00;
	cin>>num;
	int arr1[32]={0x00,};
	int arr2[4]={0x00,};

	for(int i=0;i<32;i++) arr1[31-i]=(num>>i)&0x01;
	
	for(int j=0;j<4;j++){
		int num=0x00;
		for(int k=0;k<8;k++) num=(num<<1)|(arr1[j*8+k]);
		arr2[j]=num;
	}

	int check=arr2[0]+arr2[1]+arr2[2];
	while(1){
		if(check<256){
			check=255-check;
			break;
		}
		check-=256;

	}
	if(check==arr2[3]) cout<<1<<endl;
	else cout<<0<<endl;
}
