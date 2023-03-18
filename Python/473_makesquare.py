from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        # Step1. Check if the sum of stick length can be divided by 4
        div, mod = divmod(sum(matchsticks), 4)
        if mod: return False

        # Step2. Reverse the origin list
        matchsticks.sort(reverse=True)
        targets = [div]*4

        # Step3. Fill into 4 slots until we run out of stick
        return self.backtrack(matchsticks, targets, 0, 0)

    def backtrack(self, matchsticks: List[int], targets: List[int], index: int, side: int):

        # Base case
        if side == 4 and targets[side] == 0: return True

        # General case
        matchstick = matchsticks[index]
        for i in range(side, 4):
            if matchstick <= targets[i]:
                targets[i] -= matchstick
                if self.backtrack(matchsticks, targets, index+1, i+1): return True
                targets[i] += matchstick

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.makesquare([1,1,2,2,2]))
    print(sol.makesquare([3,3,3,3,4]))