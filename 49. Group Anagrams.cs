public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var group = new Dictionary<string, List<string>>();

        foreach(string str in strs){
			var arr = str.ToCharArray();
			Array.Sort(arr);
			var key = String.Join("",arr);
			
			if(!group.ContainsKey(key)){
				group.Add(key,new List<string>()); 
			}
			
			group[key].Add(str);
			
            
        }

        var res = new List<List<string>>();
		foreach(var item in group){
			res.Add(item.Value);
		}

        return res.Cast<IList<string>>().ToList();

       
    }
    
}