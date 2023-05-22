using System;
using System.Collections.Generic;

					
public class Program
{
	 
       
	 static int LongestConsecutive(int[] nums) {
		 int res=0;
		 var itemSet = new Dictionary<int,int>();
		 
		 foreach(int num in nums)
			 itemSet[num] = 1;
		
		 for(int i=0;i<nums.Length;i++){
			 if(!itemSet.ContainsKey(nums[i]-1)){
				 int counter = 1;
				 while(itemSet.ContainsKey(nums[i]+counter))
					 counter+=1;
				res = Math.Max(res, counter);
			 }
		 }
		 
		 return res;
        
    }
	
	public static void Main()
	{	
			int[] nums  = new int[]{0,3,7,2,5,8,4,6,0,1};
			int k = 2;
			
		
			var res = LongestConsecutive(nums);
			
			Console.WriteLine(res);
		
	}
}