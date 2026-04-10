from typing import List


class Solution1:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # sort items with price in ascending order
        sorted_items = sorted(items, key=lambda x: x[0])
        # iterate through queries, and find maximum beauty in sorted_items 
        # with price lower or equal to queries[j]
        ans = []
        for q in queries:
            i = 0
            max_beauty = 0 # 1 <= beauty[i] <= 109
            while i < len(sorted_items) and sorted_items[i][0] <= q:
                max_beauty = max(max_beauty, sorted_items[i][1])
                i += 1
            ans.append(max_beauty)
        return ans
    

class Solution2:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # iterate through items, and store maximum beauty for each achievable price in bucket
        items.sort(key=lambda x: x[0])
        bucket = [[0, 0]] # [[achievable_price: maximum_beauty]]
        for price, beauty in items:
            if beauty > bucket[-1][1]:
                bucket.append([price, beauty])
        # Iterate through queries, and get maximum beauty by finding in buckest in descending order
        ans = []
        for q in queries:
            for i in range(len(bucket)-1, -1, -1):
                if bucket[i][0] <= q:
                    ans.append(bucket[i][1])
                    break
        return ans

# Example 1:
# Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
# Output: [2,4,5,5,6,6]
res = Solution2().maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6])
print(res)

# Example 2:
# Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
# Output: [4]
res = Solution2().maximumBeauty(items = [[1,2],[1,2],[1,3],[1,4]], queries = [1])
print(res)

# Example 3:
# Input: items = [[10,1000]], queries = [5]
# Output: [0]
res = Solution2().maximumBeauty(items = [[10,1000]], queries = [5])
print(res)