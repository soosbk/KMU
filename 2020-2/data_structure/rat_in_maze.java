import java.util.*;
import java.util.Stack;
// offset
//soosbk 나중에 개인포트폴리오로 활용될 소중한 자료입니다. 무단복제하지마세요

class offset{
	int a,b;

	public offset(int a, int b)
	{
		this.a=a;
		this.b=b;
	}
	public int pa(){
		return a;
	}
	public int pb(){
		return b;
	}
};


/**
 * Maze Class
 * 
 */

class Maze {
	
	private int[][] maze;	// 2 dim array for maze
	private int[][] mark;	// 2 dim array for visit marking
	Stack<Integer> stack1=new Stack<Integer>(); //i
	Stack<Integer> stack2=new Stack<Integer>(); //j
	Stack<Integer> stack3=new Stack<Integer>(); //dir
	public Maze(int m, int p) {
		maze = new int[m + 2][p + 2];
		mark = new int[m + 2][p + 2];
		for(int i = 0; i < m + 2; i++){
			for(int j = 0; j < p + 2; j++) {
				maze[i][j] = 1;
				mark[i][j] = 0;
			}
		}
				
	}

	// create the maze structure
	public void SetWall(int i, int j, int val) {
		maze[i][j] = val;
	}

	//path();
	public void Path(int m, int p) {
		offset[] move=new offset[8];
		move[0]=new offset(1,0);
		move[1]=new offset(1,-1);
		move[2]=new offset(0,-1);
		move[3]=new offset(-1,-1);
		move[4]=new offset(-1,0);
		move[5]=new offset(-1,1);
		move[6]=new offset(0,1);
		move[7]=new offset(1,1);
		int i=1,j=1;
		int g,h;
		int top=0;
		int dir=0;
		int siz=0; //stack SAVE
		int count=-1;
		mark[i][j]=1;
		stack1.push(i);
		stack2.push(j);
		stack3.push(6); //EAST
		
		while(!(stack1.empty()))
		{
			i=stack1.pop();
			j=stack2.pop();
			dir=stack3.pop();
		
			while(dir<8)
			{
				g=i+(move[dir].pa());
				h=j+(move[dir].pb());
			
				if(i==m&&j==p)
				{
					stack1.push(i);
					stack2.push(j);
					stack3.push(dir); //for stack size
					siz=stack1.size();
					String[] things=new String[siz];
					while(!(stack1.empty()))
					{
						count++;
						things[count]=("("+Integer.toString(stack1.pop())+","+Integer.toString(stack2.pop())+")");
						stack3.pop();
																	
					}
					while(count>=0){
						System.out.println(things[count]);
						count--;
					}
					return;
				}
		
		
				if(maze[g][h]==0&&mark[g][h]==0)
				{
					mark[g][h]=1;
					stack1.push(i);
					stack2.push(j);
					stack3.push(dir);
					dir=-1;
					i=g;
					j=h;
				}
				dir++;
		
			}
		}
		
		System.out.println("No path in the maze.");


	}

}; 


