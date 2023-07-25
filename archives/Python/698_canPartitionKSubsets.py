from typing import List

class Solution1:
    '''
    Time Limit Exceeded
    '''
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        # 檢查sum(nums)是否能被k整除
        div, mod = divmod(sum(nums), k)
        if mod != 0: return False
        target = [div] * k
        nums.sort(reverse=True)

        # 找出所有加總為target的組合(backtrack)
        return self.dfs(nums, k, 0, target)

    def dfs(self, nums: List[int], k: int, index: int, target: List[int]):

        # Edge case
        if index == len(nums): return True

        # Base case
        num = nums[index]
        for i in range(len(target)):
            if num <= target[i]:
                target[i] -= num
                if self.dfs(nums, k, index+1, target): return True
                target[i] += num

        return False

class Solution2:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        # 檢查sum(nums)是否能被k整除
        target, mod = divmod(sum(nums), k)
        if mod != 0: return False
        visited = [0] * len(nums)
        nums.sort(reverse=True)

        # 找出所有加總為target的組合(backtrack)
        return self.dfs(nums, k, 0, 0, 0, target, visited)

    def dfs(self, nums, k, index, _sum, count, target, visited):
        if k == 1: return True
        if _sum == target and count > 0: return self.dfs(nums, k-1, 0, 0, 0, target, visited)
        for i in range(index, len(nums)):
            if not visited[i] and _sum+nums[i] <= target:
                visited[i] == 1
                if self.dfs(nums, k, index+1, _sum+nums[i], count+1, target, visited): return True
                visited[i] == 0
        return False



if __name__ == '__main__':
    sol = Solution2()
    print(sol.canPartitionKSubsets([4,3,2,3,5,2,1], 4)) # True
    print(sol.canPartitionKSubsets([1,2,3,4], 3)) # False
    print(sol.canPartitionKSubsets([2,2,2,2,3,4,5], 4)) # False
    print(sol.canPartitionKSubsets([3,9,4,5,8,8,7,9,3,6,2,10,10,4,10,2], 10))