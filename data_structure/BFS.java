import java.util.*;

// soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요
//BFS Algorithm

// ---------- Graph class -------------

class Graph {
    int numofnodes;  // the number of nodes in the graph
    private int[][] AdjMatrix; // Adjacency matrix
    private int[] visited; // mark the visitied node


    Graph() {
        // Graph constructor. 
        numofnodes = 0;
    }

    void Init(int n) {
        numofnodes = n;
        // now create 2 dimensional array of numofnodes * numofnodes
        AdjMatrix = new int[numofnodes][numofnodes];
        visited=new int[numofnodes];
        for(int i = 0; i < numofnodes; i++) {
            // initialize all entries to 0
            for(int j = 0; j < numofnodes; j++)
                AdjMatrix[i][j] = 0;  // initialize the adjacency matrix
        }

    }


	void Edge(int n1, int n2) { 
			AdjMatrix[n1][n2]=1;
			AdjMatrix[n2][n1]=1;
			




	}

	void Bfs(int v) { 
		Queue<Integer> q = new LinkedList<>();
		for(int i=0;i<numofnodes;i++){
			visited[i]=0;}
		q.add(v);
		int data=0;
		while(!q.isEmpty()) {
			data=q.poll();
			visited[data]=1;
			System.out.print(data+"-");
			for(int i=0;i<numofnodes;i++)
			{
				if(AdjMatrix[data][i]==1&&visited[i]==0){
					q.add(i);
					visited[i]=1;}
			}
		}
		
		



	}


}
