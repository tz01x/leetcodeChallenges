class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        area_of_a = (ax2 - ax1) * (ay2 - ay1)
        area_of_b = (bx2 - bx1) * (by2 - by1)
        
        x_top_part = min(ax2, bx2)
        x_bottom_part = max(ax1, bx1)
        
        y_top_part = min(ay2, by2)
        y_bottom_part = max(ay1, by1)
        
        x_overlapping = x_top_part - x_bottom_part
        y_overlapping = y_top_part - y_bottom_part
        
        overlapping_area = 0
        if x_overlapping > 0 and y_overlapping > 0:
            overlapping_area = x_overlapping * y_overlapping

        return area_of_a + area_of_b - overlapping_area
            
        
        
        