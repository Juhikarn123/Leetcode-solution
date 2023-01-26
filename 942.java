class Solution {
    public int[] diStringMatch(String s) {
        int n=s.length();
        int[] rArr=new int[n+1];
        int lr=0;
        int hr=n;
        for(int i=0;i<n;i++)
        {
            if(s.charAt(i)=='I')
            {
                rArr[i]=lr;
                lr++;
            }
            else
            {
                rArr[i]=hr;
                hr--;
            }
        }
        rArr[n]=hr;
        return rArr;
        
    }
}