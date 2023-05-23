public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        var mapper = new Dictionary<int, int>();
        int[] result = new int[2];

        for(int i=0;i<numbers.Length;i++)
            mapper[numbers[i]] = i;
        
        for(int i=0;i<numbers.Length;i++){
            int remain = target - numbers[i];
            if(mapper.ContainsKey(remain)){
                result[0] = i+1;
                result[1] = mapper[remain]+1;
                break;
            }
        }

        return result;
        
        
    }
}