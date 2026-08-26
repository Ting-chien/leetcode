class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:

        # Transform parent list to map
        d = {}
        for c, p in enumerate(parent):
            if p != -1:
                d.setdefault(p, []).append(c)
        print(d)

        # Calculate the height of tree
        def dfs(p: int):
            # If no children, return 1
            if not d.get(p):
                return 1
            return max([dfs(c) for c in d.get(p)]) + 1
        height = dfs(0)
        print(f"height={height}")

        # Traver the tree and calculate sum
        queue = [(0, 1)] # (node, depth)
        ans = 0
        while queue:
            node, depth = queue.pop(0)
            # Update sum
            weight = nums[node] * (height - depth + 1)
            print(f"Current node={node}, depth={depth}, weight={weight}") 
            ans += (nums[node] * (height - depth + 1))
            # Add children to queue
            for c in d.get(node, []):
                queue.append((c, depth+1))

        return ans


if __name__ == "__main__":

    solution = Solution()

    # Test cases 1
    print(solution.weightedSum(parent = [-1,0,0,0,2,2], nums = [5,2,3,1,4,6])) # Output: 37

    # Test cases 2
    print(solution.weightedSum(parent = [-1,0,1,2], nums = [1,2,3,4])) # Output: 20