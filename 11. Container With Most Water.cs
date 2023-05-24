public class Solution {
    public int MaxArea(int[] height) {
        int area = 0;
        int l = 0;
        int r = height.Length - 1;
        while(l<r){
            int h = Math.Min(height[l], height[r]);
            int w = r - l;
            area = Math.Max(area, h * w);
            if(height[l]<height[r])
                l++;
            else
                r--;

        }
        return area;
    }
}