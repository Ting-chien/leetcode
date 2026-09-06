class Solution1:
    def countGoodRotations(self, nums: list[int]) -> int:

        N = len(nums)
        p1, p2 = 0, N // 2
        prefix, postfix = sum(nums[:p2]), sum(nums[p2:])

        good = 0
        while p1 < N:
            # Compare prefix and postfix
            if prefix > postfix:
                good += 1
            # Rotate
            prefix = prefix - nums[p1] + nums[p2]
            postfix = postfix - nums[p2] + nums[p1]
            # Move index
            p1 += 1
            p2 += 2

        return good


class Solution2:
    def countGoodRotations(self, nums: list[int]) -> int:

        N = len(nums)
        p1, p2 = 0, N // 2
        prefix, postfix = sum(nums[:p2]), sum(nums[p2:])

        good = 0
        while p2 < N:
            # Compare prefix and postfix
            if prefix != postfix:
                good += 1
            # Rotate
            prefix = prefix - nums[p1] + nums[p2]
            postfix = postfix - nums[p2] + nums[p1]
            # Move index
            p1 += 1
            p2 += 1

        return good