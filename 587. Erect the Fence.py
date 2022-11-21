from typing import List

def cross_product(p1, p2):
	return p1[0] * p2[1] - p2[0] * p1[1]

def direction(p1, p2, p3):
	return  cross_product([p3[0] - p2[0] , p3[1]-p2[1]], [p2[0] - p1[0] , p2[1]-p1[1]])

def is_left(p1, p2, p3):
	return direction(p1, p2, p3) < 0

def outerTrees(trees: List[List[int]]):
    trees.sort(key=lambda p:p[0])
    stack_lower=[trees[0],trees[1]]
    stack_top=1
    for i in range(len(trees)):
        if is_left(stack_lower[stack_top-1],stack_lower[stack_top],trees[i]):
            stack_lower.append(trees[i])
            stack_top+=1
        else:
            stack_lower[stack_top]=trees[i]
            
    print(stack_lower)
        
    

outerTrees(
    [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
)