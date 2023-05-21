using System;
using System.Collections.Generic;

					
public class Program
{
	 static int[] TopKFrequent(int[] nums, int k) {
		 var table = new Dictionary<int,int>();
		 foreach(int num in nums){
			 if(!table.ContainsKey(num))
				 table.Add(num,0);
			table[num]+=1;
		 }
		 
		 List<int>[] bucketSortArray = new List<int>[nums.Length+1];
		 
		 foreach(var item in table){
		 	if(bucketSortArray[item.Value]==null){
			bucketSortArray[item.Value] = new List<int>();
			}
		      
			bucketSortArray[item.Value].Add(item.Key);
		 }
		
		
		 int[] topKItems= new int[k];
		 int counter = 0;
		 
		 for(int i=bucketSortArray.Length -1;i>0&&k>0 ;i--){
			 
			 if(bucketSortArray[i]!=null){
				 foreach(int item in bucketSortArray[i]){
					 
					 
					 if(counter < k){
						topKItems[counter] = item;
					 counter+=1;
					 }
				 }
			 }
		 	
		 }
		 
       
		 return topKItems;
    }
	
	public static void Main()
	{	
			int[] nums  = new int[]{1};
			int k = 2;
		
			var res = TopKFrequent(nums, k);
			foreach(int v in res)
				Console.WriteLine(v);
		
	}
}