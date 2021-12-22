#include<iostream>
using namespace std;

int M[102][102];
int d[102];
int main(){
	int time;
	int n;
	int j;
	int tmp,min;
	scanf("%d",&time);
	for(int t=0;t<time;t++){
		scanf("%d",&n);
		for(int num=0;num<=n;num++) scanf("%d",&d[num]);
		for(int i=1;i<=n;i++) M[i][i]=0;  //n+1
			
		for(int dg=1;dg<=n-1;dg++){
			for(int i=1;i<=n-dg;i++){
				j=i+dg;
				min=M[i][i]+M[i+1][j]+d[i-1]*d[i]*d[j];

				for(int k=i+1;k<=j-1;k++) {
					tmp=M[i][k]+M[k+1][j]+d[i-1]*d[k]*d[j];
					if(min>tmp) min=tmp;
				}

				M[i][j]=min;
			}
		}

		printf("%d\n",M[1][n]);
		
		
	}	

	
}
