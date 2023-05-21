using System;
using System.Collections.Generic;

					
public class Program
{
	 
       
	 static int[] ProductExceptSelf(int[] nums) {
        int[] answer = new int [nums.Length];
		int tmp = 1;
		 answer[0] = 1;
		for(int i=1;i<nums.Length;i++){
			answer[i] = nums[i-1] * answer[i-1];
		}
		for(int i=nums.Length-1; i>=0;i--){
			
			answer[i] = answer[i] * tmp;
			tmp = nums[i] * tmp;
			
		}
		return answer;
    }
	
	public static void Main()
	{	
			int[] nums  = new int[]{1,2,3,4};
			int k = 2;
			
		
			var res = ProductExceptSelf(nums);
			foreach(int v in res)
				Console.WriteLine(v);
		
	}
}