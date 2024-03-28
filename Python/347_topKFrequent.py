from typing import List

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Turn nums into a dict structure
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        # Find the top `k` element in the dict
        sorted_d = {k: v for k, v in sorted(d.items(), key=lambda kv: kv[1], reverse=True)}
        return list(sorted_d.keys())[:k]

if __name__ == '__main__':
    sol = Solution1()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1], 1))