class Solution {
    public int maxProfit(int[] prices) {
        int mp=Integer.MAX_VALUE;
        int profit=0;
        for(int i=0;i<prices.length;i++)
        {
            mp=Math.min(mp,prices[i]);
            profit=Math.max(prices[i]-mp,profit);
        }
        return profit;
        
    }
}