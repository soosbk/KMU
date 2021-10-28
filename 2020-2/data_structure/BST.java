import java.util.*;

// soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요
// Binary Search Tree

@SuppressWarnings("unchecked")
class BST <T extends KeyValue> {
	class TreeNode <U extends KeyValue> {
		U data;	// storage for data : in HW 3, T will be Item
		TreeNode<U> leftChild;	// link to the left Child
		TreeNode<U> rightChild;	// link to the right Child

		// constructors come here
		TreeNode() {
			leftChild = rightChild = null;
		}
		TreeNode(U d) {
			// data is given
			data = d;
			// the leftChild and rightChild field are null
			leftChild = rightChild = null;
		}
	};

	TreeNode <T> root;
	BST() { 
		// BST constructor. 
		root = null;
	}

	void Show() {
		System.out.print( "PRE  Order : ");
		PreOrder(root);
		System.out.println("");
		System.out.print("IN   Order : ");
		InOrder(root);
		System.out.println("");
		System.out.print("POST Order : ");
		PostOrder(root);
		System.out.println("");
		System.out.print("Number of Nodes : ");
		System.out.println( Count(root));
		System.out.print("HEIGHT : ");
		System.out.println( Height(root));
		System.out.println("");
	}

	boolean  Insert(T item)  {
		// first search the key
		if(Get(item)!=null) return false;
		if(root == null) {
			root =  new TreeNode<T>(item);
			return true;
		}
		TreeNode<T> ptr, parent;
		ptr=root;
		
		
		while(true){
			parent=ptr;
			if(item.GetKey()>parent.data.GetKey())
         		{
            			ptr=parent.rightChild;
            			if(ptr==null) {
               				parent.rightChild=new TreeNode<T>(item);
					break;
            			}
        		 }
         
         		else {
            			ptr=parent.leftChild;
            
            			if(ptr==null) {
              				parent.leftChild=new TreeNode<T>(item);
					break;
            			}
			}

		}
		return true;
	}

	T Get(T item)  {
		// use the key field of item and find the node
		// do not use val field of item
		TreeNode<T> ptr;
		ptr = root;
		if(root==null) return null;

		
		while(true)
		{
			if(ptr.data.GetKey()==item.GetKey()) break;
			else if(ptr.data.GetKey()<item.GetKey())
				ptr=ptr.rightChild; 
			else
				ptr=ptr.leftChild;

			if(ptr==null)
				return null;
		}
		
		
		return ptr.data;
	} 


	boolean Delete(T item)  {
		if(root == null)
			return false;	// non existing key

		//no element with delete key
		if(Get(item)==null) return false; 

		TreeNode<T> current, parent;
		parent=root;
		
		
		while(true){
			if(root.data.GetKey()==item.GetKey()){
				current=root;
				break;
			}
         		else if(parent.data.GetKey()>item.GetKey()){
            			if(parent.leftChild.data.GetKey()==item.GetKey()){
               				current=parent.leftChild;
               				break;
            			}
            			else parent=parent.leftChild;
         		}
         		else if(parent.data.GetKey()<item.GetKey()){
            			if(parent.rightChild.data.GetKey()==item.GetKey()){
               				current=parent.rightChild;
               				break;}
            			else parent=parent.rightChild;
         		}
      		}

		//child x
		if(current.leftChild==null&&current.rightChild==null){
			if(root==current) root=null;			
			else if(parent.leftChild==current) parent.leftChild=null;
			else parent.rightChild=null;}
		//child 1
		else if(current.leftChild==null){
			if(root==current) root=root.rightChild;
			else if(parent.leftChild==current) parent.leftChild=current.rightChild;
			else  parent.rightChild=current.rightChild;
		}
		else if(current.rightChild==null){
			if(root==current) root=root.leftChild;
			else if(parent.leftChild==current) parent.leftChild=current.leftChild;
			else  parent.rightChild=current.leftChild;}
		//child2
		else{
			//Find_max
			TreeNode<T> max, max_p;
         		max=current.leftChild;
         		max_p=current.leftChild;
	       		TreeNode<T> ptr=current.leftChild;
         		while(true){
				if(ptr.rightChild==null) break;
				max_p=max;
				max=ptr.rightChild;
				ptr=ptr.rightChild;
			
			}
			if(ptr==current.leftChild){
				if(root==current){
					root.leftChild=ptr.leftChild;
					root=max;}
				else if(parent.leftChild==current){
					current.leftChild=max.leftChild;
					parent.leftChild=max;}
				else{
					current.leftChild=max.leftChild;
					parent.rightChild=max;}
         		}
			else{
				max_p.rightChild=max.leftChild;
				max.leftChild=current.leftChild;
				max.rightChild=current.rightChild;
				if(root==current){
					root=max;}
				else if(parent.leftChild==current){
					
					parent.leftChild=max;}
				else parent.rightChild=max;
			}
		}
		



		
		return true;

	}

	void  PreOrder(TreeNode<T> t)  {

		if(t!=null)
		{
			System.out.print("["+t.data.GetKey()+"("+t.data.GetValue()+")"+"]");
			PreOrder(t.leftChild);
			PreOrder(t.rightChild);
		}
	}

	void  InOrder(TreeNode<T> t)  {
		if(t!=null)
		{
			InOrder(t.leftChild);
			System.out.print("["+t.data.GetKey()+"("+t.data.GetValue()+")"+"]");
			InOrder(t.rightChild);
		}


	}

	void  PostOrder(TreeNode<T> t)  {
		if(t!=null)
		{
			PostOrder(t.leftChild);
			PostOrder(t.rightChild);
			System.out.print("["+t.data.GetKey()+"("+t.data.GetValue()+")"+"]");
		}


	}

	int  Count(TreeNode<T> t)  {
		if(t==null) return 0;
		else
		{
			if(t.leftChild==null &&t.rightChild==null) return 1;
			else
				return (1+Count(t.leftChild)+Count(t.rightChild));
		}
	}

	int  Height(TreeNode<T> t)  {
		if(t==null) return 0;
		

		return (1+Math.max(Height(t.leftChild),Height(t.rightChild)));


	}
}

