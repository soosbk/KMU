//원형큐 (Circular Queue)를 구현
// soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요
import java.util.*;

/**
 * Generic version of the MyQueue class.
 * @param <T> the type of the value being queued
 */

class MyQueue <T> {
	private T[] queue;	// array for queue elements
	private int front, // one counterclockwise from front
	            rear, 	// array position of rear element
				capacity;	// capacity of queue array

	/**
	 * Create an empty queue whose initial capacity is cap
	 */
	@SuppressWarnings("unchecked")
	MyQueue(int cap) {
		capacity = cap;
		queue = (T []) new Object [capacity];
		front = rear = 0;
	}

	/** 
	 * If number of elements in the queue is 0, return true else return false
	 */
	boolean IsEmpty() {

// NEED TO IMPLEMENT

		if(front == rear)
			return true;
		else
			return false;
	}

	/**
	 * Add x at rear of queue
	 */
	void Push (T x) throws Exception { 

// NEED TO IMPLEMENT
		if((rear+1)%capacity==front)
		{
			

		// if queue full, throw the following message
			throw new Exception ("Queue is Full");
		}
		rear=(rear+1)%capacity;
		queue[rear]=x;
	}

	/**
	 * Delete front element from queue
	 */
	T Pop() throws Exception {
		// if queue is empty, throw the following message
		if(IsEmpty())			
			throw new Exception("Queue is empty. Cannot delete.");
		else{
	
			front=(++front)%capacity;
			return queue[front];
		}

	}
	
  
  //
	public String toString() {
		String a = new String();

		a = "MyQueue : ";

		int f=front;
		while(f!=rear){
			f=(f+1)%capacity;
			a=a+queue[f]+" ";
		}
		a=a+"\n"+"rear="+rear+", front="+front;
		return a;
	}	
}; 

