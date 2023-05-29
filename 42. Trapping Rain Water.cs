public class Solution {
    public int Trap(int[] height) {
        int n = height.Length;
        int[] leftMax = new int [n];
        int[] rightMax = new int[n];
        leftMax[0] = 0;
        rightMax[n-1] = 0;
        for(int i=1;i<n;i++){
            leftMax[i] = Math.Max(leftMax[i-1], height[i-1]);
            rightMax[n-1-i] = Math.Max(rightMax[n-i], height[n-i]);
        }
        int counter = 0;
        for(int i=0;i<n;i++){
           int rem =  Math.Min(leftMax[i], rightMax[i]) - height[i];
           if (rem>0){
               counter+=rem;
           }
        }
        return counter;
        
    }
}