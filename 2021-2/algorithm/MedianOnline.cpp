#include<iostream>
#include<vector> //minheap과 maxheap에서 배열 대신 사용(그 외에는 사용하지 않음)

using namespace std;




class Heap{
private:
	bool odd=true;
	unsigned int min=0,max=0;
	unsigned int median=0;
	unsigned long int median_sum=0;
	vector<unsigned int> min_h; int min_siz=0; //right
	vector<unsigned int> max_h; int max_siz=0; //left
	
	
public:
	Heap(unsigned int n): min_h(n/2+1,0),max_h(n/2+1,0){}

	void swap(bool type,int idx1,int idx2){
		if(type){
			int tmp=min_h[idx1];
			min_h[idx1]=min_h[idx2];
			min_h[idx2]=tmp;
		}

		else{
			int tmp=max_h[idx1];
			max_h[idx1]=max_h[idx2];
			max_h[idx2]=tmp;
		}
		
	}

	void cal_mid(){
		if(min_siz!=max_siz) median=min_h[1];
		
		else median=(min_h[1]+max_h[1])/2;
		median_sum+=median;
		
	}
	void caller(int d){
		if(min_siz==max_siz){ //홀수
			if(median<=d) push_min(d);
			
			
			else{
				push_min(max_h[1]);
				pop_max();
				push_max(d);
				
			}
		}

		else{//짝수
			if(median<d){
				push_max(min_h[1]);
				pop_min();
				push_min(d);
				
			}
			else push_max(d);
				
			
		}
		
		
				
		cal_mid();
		
	}
	void push_min(int d){
		min_h[++min_siz]=d;
		int ch=min_siz;
		int pa=ch/2;
		while(ch>1&&min_h[ch]<min_h[pa]){
			swap(true,ch,pa);
			ch=pa;
			pa=ch/2;
		}
		
		
	}
	void push_max(int d){
		max_h[++max_siz]=d;
				
		int ch=max_siz;
		int pa=ch/2;
		while(ch>1&&max_h[ch]>max_h[pa]){
			swap(false,ch,pa);
			ch=pa;
			pa=ch/2;
		}

		
		
	}

	void pop_min(){
		swap(true,1, min_siz);
    	min_siz-=1;
    
    	int pa = 1;
    	int ch = pa*2;
    
    	if(ch+1 <= min_siz){
       		if(min_h[ch]>min_h[ch+1]) ch+=1;
    	}
    
    	while(ch<=min_siz && min_h[ch]<min_h[pa]){
    		swap(true,ch, pa);
	        pa = ch;
	        ch = pa*2;
	        
	        if(ch+1 <= min_siz){
	        	if(min_h[ch]>min_h[ch+1]) ch+=1;
	            
	        }

		}
		
	}


	void pop_max(){
		swap(false,1, max_siz);
    	max_siz-=1;
    
    	int pa = 1;
    	int ch = pa*2;
    
    	if(ch+1 <= max_siz){
       		ch = (max_h[ch]>max_h[ch+1]) ? ch : ch+1;
    	}
    
    	while(ch<=max_siz && max_h[ch]>max_h[pa]){
    		swap(false,ch, pa);
	        pa = ch;
	        ch = pa*2;
	        
	        if(ch+1 <= max_siz){
	        	if(max_h[ch]<max_h[ch+1]) ch+=1;
	        }

		}
		
	}
	int return_median_sum(){
		return median_sum%10;
	}
};
	




int main(){
	int t;
	int k,num;
	unsigned int tmp;
	unsigned long long int median_sum;

	cin>>t;
	for(int i=0;i<t;i++){
		median_sum=0;
		cin>>num;
		Heap h(num);
		for(int j=0;j<num;j++){
			cin>>tmp;
			h.caller(tmp);
		}
		cout<<h.return_median_sum()<<endl;

	}

}

