#include<iostream>
#include<vector>
#include<string>
using namespace std;
int swapnum_H=0;
int comparenum_H=0;
int swapnum_L=0;
int comparenum_L=0;

vector<int>v1(1000);
vector<int>v2(1000);
int num;



int partition_hoare(int low,int high){
	int pivot=v1[low];
	int i=low-1; int j=high+1;
	while(true){
		do {
			i+=1;
			comparenum_H+=1;
			
		}while(v1[i]<pivot);
		do{
			
			
			j-=1;
			comparenum_H+=1;
			
		}while(v1[j]>pivot);
		if(i<j){
			int tmp=v1[i];
			v1[i]=v1[j];
			v1[j]=tmp;
			swapnum_H+=1;
			
		}
		
		else return j;
		
	}

	
}

int partition_Lomuto(int low, int high){
	int pivot=v2[low];
	int j=low;
	for(int i=low+1;i<=high;i++){
		comparenum_L+=1;
		if(v2[i]<pivot){

			j+=1;
			int tmp=v2[i];
			v2[i]=v2[j];
			v2[j]=tmp;
			swapnum_L+=1;
		}
	}
	
	int pivot_pos=j;
	int tmp=v2[pivot_pos];
	v2[pivot_pos]=v2[low];
	v2[low]=tmp;
	swapnum_L+=1;
	return pivot_pos;
}


void quicksort(int low,int high){
	int p;
	if (low>=high) return;
	
	p=partition_hoare(low,high);
	quicksort(low,p);
	quicksort(p+1,high);
	
}
void quicksort2(int low,int high){
	int p;
	if (low>=high) return;
	
	p=partition_Lomuto(low,high);
	quicksort2(low,p-1);
	quicksort2(p+1,high);
	
}

int main(){
	int t;
	int tmp;
	cin>>t;
	for(int i=0;i<t;i++){
		int k=0;
		swapnum_H=0;
		comparenum_H=0;
		swapnum_L=0;
		comparenum_L=0;
		cin>>num;
		
		for(int j=0;j<num;j++) {
			cin>>tmp;
			v1[k]=tmp;
			v2[k++]=tmp;
		}
		quicksort(0,num-1);
		quicksort2(0,num-1);
		cout<<swapnum_H<<" "<<swapnum_L<<" "<<comparenum_H<<" "<<comparenum_L<<endl;
		
		

	}
}
