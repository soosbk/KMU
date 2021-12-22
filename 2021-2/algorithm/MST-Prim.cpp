#include<iostream>
#include<vector>
using namespace std;



int prim(vector < vector <int> > &weight,int n){
	vector<int> nearest(n+1,1000000);
	vector<int> d(n+1,1000000);

	int vnear=0;
	int return_val=0;
	for(int i=2;i<=n;i++){
		nearest[i]=1;
		d[i]=weight[1][i];
	}
	for(int time=0;time<n-1;time++){
		int min_num=1000000;
		for(int i=2;i<=n;i++){
			if((d[i]>=0)&&(d[i]<min_num)){
				min_num=d[i];
				vnear=i;
			}
		}
		return_val+=d[vnear];
		d[vnear]=-1;

		for(int i=2;i<=n;i++){
			if(weight[i][vnear]<d[i]){
				d[i]=weight[i][vnear];
				nearest[i]=vnear;
			}
		}
	}
	return return_val;

}

int main(){
	int case_num;
	int node;
	int return_val;
	int tmp1,tmp2;
	int t;
	int vnear;

	scanf("%d",&case_num);
	for(int cn=0;cn<case_num;cn++){
		scanf("%d",&node);
		vector<vector<int>> weight(node+1,vector <int>(node+1,1000000));
	
		for(int i=1;i<=node;i++){
			scanf("%d%d",&tmp1,&t);
			for(int j=1;j<=t;j++) 
			{
				scanf("%d%d",&tmp1,&tmp2);
				
				weight[i][tmp1]=tmp2;
			}
				

		}

		return_val=prim(weight,node);
		
		printf("%d\n", return_val);
	
	}
}



