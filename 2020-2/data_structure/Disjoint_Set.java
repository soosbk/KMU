// Lab 007	: Disjoint Sets
// soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요


import java.util.*;


class DisjointSets {
	int numofelements;  // the total number of elements in all the disjoint sets
	private int[] parent; // maintains the parent pointer of each element in the disjoint sets
	private int[] weight; // maintains the weight of each set


	DisjointSets() { 
		// DisjointSets constructor. 
	}

	public String toString() { // Show all the element in sequence
		String str = new String();
	    // Show the array elements in parent[]

		str = "parent[]: - ";
		for(int i = 1; i <= numofelements; i++)
			str += parent[i] + " ";
		return str;
	}

	void InitSet(int n) { 
		// Initialize the array parent[] and weight[]

		numofelements=n;
		parent=new int[n+1];
		weight=new int[n+1];
		for(int i=0;i<=n;i++){
			parent[i]=0;
			weight[i]=1;
		}
		
	}

	boolean Union(int i, int j) { 
	// Union the set that contains i and the set that contains j
	// the set that has larger weight is the new root of the unioned set
	// when the weights are the same, choose the root of smaller value

		// first find the root of i and j
				
		int x=SimpleFind(i);  //root of i=x
		int y=SimpleFind(j);  //root of j=y
		
		if(x==y) return false;
	
		if (weight[x]>weight[y]){
			parent[y]=x;
			weight[x]+=weight[y];
		}
			
		else if(weight[x]==weight[y])
		{
			if(x>y){
				parent[y]=x;
				weight[x]+=weight[y];
			}
	
			else{
				parent[x]=y;
				weight[y]+=weight[x];
			}
		}
			
		else{
			parent[x]=y;
			weight[y]+=weight[x];
		}
		
		return true;
		
		}
		

	int SimpleFind(int i) { 
	// return the root node that contains the element i

		
		while(parent[i]>0){
			if(i==parent[i]) break; 
			i=parent[i];
			
		}
		int root = i;
		return root;
			
	}
}
