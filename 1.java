class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer>map=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++)
        {
            int t=target-nums[i];
           if(map.containsKey(t))
           {
               return new int[]{i,map.get(t)};
           }
            else
            {
                map.put(nums[i],i);
            }
        }
        return new int[]{};
        
    }
}