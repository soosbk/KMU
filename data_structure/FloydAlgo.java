// Lab 009	: Graph Floyd Algorithm 
// soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요


import java.util.*;


class Graph {
	int numofnodes;  // the number of nodes in the graph
	private int[][] CostAdj; // Adjacency matrix
	private int[] dist; // dist array
	private int[] p; // p array

	final int LargeCost = 999999;

	Graph() { 
		// Graph constructor. 
		numofnodes = 0;
	}


	void Init(int n) { 
		numofnodes = n;
		// now create 2 dimensional array of numofnodes * numofnodes
		CostAdj = new int[numofnodes][numofnodes];
		dist = new int[numofnodes];
		p = new int[numofnodes];

		for(int i = 0; i < numofnodes; i++) {
			// initialize all entries to 0
			for(int j = 0; j < numofnodes; j++)
				CostAdj[i][j] = LargeCost;  // initialize the adjacency matrix
			CostAdj[i][i] = 0;
		}
	}
	public String toString() { 
		String str;
		int i = 0;
		str = "Dist : ";
		for(i = 0; i < numofnodes; i++)
			str +=  dist[i] + " ";
		str += "\n";
	
		str += "P    : ";
		for( i = 0; i < numofnodes; i++)
			str += p[i] + " ";
		str += "\n";
	
		// show the paths to all the destinations
		for( i = 0; i < numofnodes; i++) {
			str += "Path => " + i + " : ";
			str += OutPath(i);	
			str += "\n";
		}
		return str;
	}



	void Edge(int v1, int v2, int cost) { 
		// NEED TO IMPLEMENT

		CostAdj[v1][v2]=cost;
		

	}


	String OutPath(int i) { 
		String str = "";
		
		while(true){
			if(p[i]==-1){
				str+=i+" ";
				break;}	
			else{
				str+=OutPath(p[i])+i+" ";
				break;
						
			}
		
				
		 }
		
		return str;
	}

	void BellmanFord(int v) { 
		
		// NEED TO IMPLEMENT
		
		for(int i=0;i<numofnodes;i++) {
			if(i==v) dist[i]=0;
			else dist[i]=LargeCost;
			p[i]=-1;
		}
		
		
		for(int k=1;k<numofnodes;k++) {  
			for(int i=0;i<numofnodes;i++) {

				for(int w=0;w<numofnodes&&i!=v;w++) {
						if(dist[i]>(dist[w]+CostAdj[w][i])) {
								dist[i]=dist[w]+CostAdj[w][i];
								p[i]=w;
								
						}
							
				}
			}
				
		}

	}
}




