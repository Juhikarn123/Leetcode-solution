class Solution {
    public int[] numberOfPairs(int[] nums) {
        int[] freq=new int[101];
        for(int num:nums)
        {
            freq[num]++;
        }
        int pc=0;
        for(int i=0;i<101;i++)
        {
            pc+=freq[i]/2;
        }
        return new int[]{pc,nums.length-2*pc};
        
    }
}