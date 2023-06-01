

public class MinStack {
        int topIdx;
        List<int> arr;
        List<int> curr_min;

    public MinStack() {
        this.topIdx = -1;
        this.arr = new List<int>();
         this.curr_min = new List<int>();
    }
    
    public void Push(int val) {
        
       if(this.topIdx==-1){
            this.curr_min.Add(val);
       }else{
           int minVal = Math.Min(val, this.curr_min[this.topIdx]);
            this.curr_min.Add(minVal);
       }
       this.arr.Add(val);
       this.topIdx+=1;
    }
    
    public void Pop() {
        this.arr.RemoveAt(this.topIdx);
        this.curr_min.RemoveAt(this.topIdx);
        this.topIdx-- ;
    }
    
    public int Top() {
        return this.arr[this.topIdx];
    }
    
    public int GetMin() {
        return this.curr_min[this.topIdx];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */