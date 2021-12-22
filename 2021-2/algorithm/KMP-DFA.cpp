#include<iostream>
#include<string>
#include<set>
using namespace std;

int dfa[3][1002];
void con_dfa(string pattern,int r, int patlen){
	dfa[0][0]=0;dfa[1][0]=0;dfa[2][0]=0;
	dfa[pattern[0]-65][0]=1;
	int x=0,cnt=0;
	for(int j=1;j<patlen;j++){
		for(int c=0;c<r;c++) dfa[c][j]=dfa[c][x];

		dfa[pattern[j]-65][j]=j+1;
		x=dfa[pattern[j]-65][x];
	}

	for(int c=0;c<r;c++) dfa[c][patlen]=dfa[c][x];


	
	for(int i=0;i<r;i++){
		for(int j=0;j<=patlen;j++){
			if(dfa[i][j]!=0) cnt++;
		}
	}
	printf("%d ",cnt);

}


void kmp(string txt,int patlen){
	int txtlen=txt.size();
	int j=0,cnt=0;
	for(int i=0;i<txtlen;i++){
		j=dfa[txt[i]-65][j];
		if(j==patlen) cnt+=1;
	}
	printf("%d\n",cnt);
}

int main(){
	int case_num;
	scanf("%d",&case_num);
	for(int case_n=0;case_n<case_num;case_n++){
		string pat;
		string txt;
		set<char> s;
		cin>>pat>>txt;
		for(int i=0;i<txt.size();i++){
			s.insert(txt[i]);
		}
		int patlen=pat.size();
		//cout<<patlen;
		con_dfa(pat,s.size(),patlen);
		kmp(txt,patlen);
	}
}
