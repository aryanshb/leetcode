# [121] Best Time to Buy and Sell Stock

**[array, dynamic-programming]**

### Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.


**Example 1:**

```

**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

**Example 2:**

```

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit = 0.

```

**Constraints:**
* `1 <= prices.length <= 105`
* `0 <= prices[i] <= 104`


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            profit = prices[i] - a
            
            if profit>maxprofit:
                maxprofit = profit
                
            if a>prices[i]:
                a = prices[i]
        return maxprofit
        
```

<br>

### Statistics

- total accepted: 2577166
- total submissions: 4739061
- acceptance rate: 54.4%
- likes: 19466
- dislikes: 624

<br>

### Similar Problems

- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray) (Medium)
- [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii) (Medium)
- [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii) (Hard)
- [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv) (Hard)
- [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) (Medium)
- [Sum of Beauty in the Array](https://leetcode.com/problems/sum-of-beauty-in-the-array) (Medium)
- [Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements) (Easy)
- [Maximum Profit From Trading Stocks](https://leetcode.com/problems/maximum-profit-from-trading-stocks) (Medium)
