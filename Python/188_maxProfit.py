from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """Dynamic Programming (bottom-up)
        
        For k=2, prices=[3,2,6,5,0,3]

        max=0
        day=2, spread=2-3=-1, max=0||0+(-1)=0
        day=3, spread=6-2=4, max=0||0+4=4
        day=4, spread=5-6=-1, max=4||4+(-1)=4
        ...
        """
        times = 0
        curr_max = 0
        for i in range(1, len(prices)):
            if times >= k: break
            spread = prices[i] - prices[i-1]
            # curr_max = max(curr_max, curr_max+spread)
            # TODO How to count transaction times ?
            # Option1. curr_max+spread > curr_max ? No, 有可能會連續升息好幾次
            if curr_max + spread > curr_max:
                curr_max = curr_max + spread
                if i < len(prices)-1 and prices[i] > prices[i+1]:
                    times += 1

        return curr_max
        

if __name__ == '__main__':

    s = Solution()
    print(s.maxProfit(k=2, prices=[2,4,1])) # Output=2
    print(s.maxProfit(k=2, prices=[3,2,6,5,0,3])) # Output=7
    print(s.maxProfit(k=2, prices=[6,1,3,2,4,7])) # Output=7
    print(s.maxProfit(k=2, prices=[3,3,5,0,0,3,1,4])) # Output=6