// Lab 10: Natural Merge
// soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요



import java.util.*;


class NaturalMerge {
	int noe;  // the number of elements
	private int[] inputArray; // input array 
	int[] outputArray; // output array 


	NaturalMerge() { 
		noe = 0;
	}

	void Init(int [] arr, int n) { 
		noe = n;
		inputArray = new int[noe];
		System.arraycopy(arr, 0, inputArray, 0, n);

		outputArray = new int[noe];
	}

	void Merge() { 
		int m = 0;
		for(int i=1;i<noe;i++) {
			if(inputArray[i]<inputArray[i-1]) m=i; 
		}
		System.out.println("m = " + m + ", n = " + noe);
		int index1=0;
		int index2=m;
		int t=0;
		
		while((index1<m) && (index2<noe)) {
			
			if(inputArray[index1]<inputArray[index2]) { 
				outputArray[t++]=inputArray[index1++];
			}
			else if(inputArray[index1]==inputArray[index2]) {
				outputArray[t++]=inputArray[index1++];
				outputArray[t++]=inputArray[index2++];

			}
			else {
				outputArray[t++]=inputArray[index2++];
			}
		}
		
		for(;index1<m;index1++) {
			outputArray[t++]=inputArray[index1];}
		for(;index2<noe;index2++) {
			outputArray[t++]=inputArray[index2];}
		
		
		// NEED TO IMPLEMENT


	}
}

