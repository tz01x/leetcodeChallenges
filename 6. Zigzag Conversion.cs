using System;
using System.Collections.Generic;
					
public class Program
{
	public class IteratorCount {
		public int x;
		public int y;
		public IteratorCount(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

	}
	static string Convert(string s, int numRows) {
		int b =  Math.Abs(numRows - 3) + 1;
		int x = numRows + b;
		if (numRows < 2){
			return s;
		}
		if(numRows==2){
			x = 2;
		}
		
		IteratorCount [] patttern = new IteratorCount [numRows];
		int k = x;
		int m = 0;
		for(int i=0;i<numRows;i++){
			
			patttern[i] = new IteratorCount(x,m);
			m+=2;
			x-=2;
			if (x==0){
			x=k;
			m=k;
		}
			
		}
		string new_str = "";
		for(int i=0;i<patttern.Length;i++){
			var counter = patttern[i];
			Console.WriteLine(counter.x.ToString() + " " + counter.y.ToString());
			int alternator = 0;
			for(int j=i;j<s.Length;){

				new_str += s[j];
			if(alternator==0 || counter.y == 0){
				j+=counter.x;
				alternator=1;
			}else{
				j+=counter.y;
			alternator=0;
			}
				
			}
			
		}
		
		
		return new_str;
        
    }
	public static void Main()
	{
		int[] arr = new int[]{24,13,1,100,0,94,3,0,3};
		
		
		Console.Write(Convert("PAYPALISHIRING", 6));
		//PAHNAPLSIIGYIR
		
	}
}