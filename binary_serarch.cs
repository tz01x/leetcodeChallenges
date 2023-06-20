using System;
using System.Collections.Generic;
					
public class Program
{
	public static int Search(int[] nums, int target) {
		int l = 0;
		int r = nums.Length -1;
	
		while(l<=r){
		int mid =(l+r)/ 2 ;
		
		if(nums[mid] == target){
			return mid;
		}
			
		else if(nums[mid]<target){
			l = mid + 1;		
		}else{
		r = mid -1;
		}
       
    }
		return -1;
	}
	public static void Main()
	{
		int[] arr = new int[]{-1,0,3,5,9,12};
		
		
		Console.Write(Search(arr, -8));
		
	}
}