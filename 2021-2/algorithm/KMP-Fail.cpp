#include<iostream>
#include<string>
#include<vector>

using namespace std;


vector<int> getfail(string pat){
	int m=pat.size();
	int j=0;
	vector<int> fail(m,0);


	for(int i=1;i<m;i++){
		while(j>0 && pat[i]!=pat[j]) j=fail[j-1];
		if(pat[i]==pat[j]) fail[i]=++j;
	}
	return fail;
}


void kmp(string txt,string pat){
	vector<int>fail=getfail(pat);
	int txtlen=txt.size();
	int patlen=pat.size();
	int cnt=0;
	int j=0;
	for(int i=0;i<txtlen;i++){
		while(j>0&&txt[i]!=pat[j]) j=fail[j-1];
		if(txt[i]==pat[j]){
			if(j==patlen-1){
				cnt++;
				j=fail[j];
			}
			else j++;
		}
		
	}
	for(int i=0;i<patlen;i++) printf("%d ",fail[i]);
	printf("\n%d\n",cnt);
}

int main(){
	int case_num;
	scanf("%d",&case_num);
	for(int case_n=0;case_n<case_num;case_n++){
		string pat;
		string txt;
		cin>>pat>>txt;
		kmp(txt,pat);
		
		
	}
}
