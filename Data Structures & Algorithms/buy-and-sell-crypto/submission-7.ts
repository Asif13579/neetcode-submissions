class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let n: number=prices.length;
        if (n<2) return 0;
        let minPrice: number=prices[0];
        let maxProfit: number=0;
        for (let i=0; i<n;i++) {
            minPrice=Math.min(minPrice,prices[i]);
            maxProfit=Math.max(maxProfit,prices[i]-minPrice);
        }
        return maxProfit;
    }
}
