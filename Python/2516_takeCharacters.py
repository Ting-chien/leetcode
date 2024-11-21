class Solution1:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        Approach 1. Recursion (Time Limit Exceed)

         - Time Compexity: O(2^n)
         - Space Compexity: O(n)
        """
        
        res = float('inf')
        def dfs(s: str, count: dict, minutes: int):
            """
            :param s: 可被選擇的字串
            :param count: 各個字串被取得的次數
            :param minutes: 取得當前字元次數所需花費的時間
            """
            # 當 a, b, c 三個字元都出現 k 次以上，則計算當前花費的最少時間並返回
            if count["a"] >= k and count["b"] >= k and count["c"] >= k:
                nonlocal res
                res = min(res, minutes)
                return

            # 當 s 已經被取完
            if not s: 
                return

            # 從左側取
            copy_c = count.copy()
            copy_c[s[0]] += 1
            dfs(s[1:], copy_c, minutes+1)

            # 從右側取
            copy_c = count.copy()
            copy_c[s[-1]] += 1
            dfs(s[:-1], copy_c, minutes+1)

        dfs(s=s, count={"a": 0, "b": 0, "c": 0}, minutes=0)
        return -1 if res == float('inf') else res
    

class Solution2:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        Approach 2. Sliding Window
        
         - Time Compexity: O(n)
         - Space Compexity: O(1)
        """
        # 先檢查 s 中是否 a, b, c 都有出現 k 次以上
        # 若沒有則返回 -1
        count = [0] * 3
        for c in s:
            count[ord(c)-ord("a")] += 1
        for val in count:
            if val < k:
                return -1
        # 透過 sliding window 尋找最大的可不被包含在內的視窗
        # 視窗內的字元是不被選取的，因此，隨著右指真相右視窗變大，選中的字元數量變少
        # 為了達到平衡，當字元數量少於 k 時，左指針就會向右移來縮小視窗
        # 並且在每次視窗移動時找到最大的視窗
        window = [0] * 3
        left, max_window = 0, 0
        for right in range(len(s)):
            # 計算當前 window 中字元的數量
            window[ord(s[right])-ord("a")] += 1
            # 檢查是否符合 a, b, c 次數至少為 k
            while left <= right and (
                count[0] - window[0] < k \
                or count[1] - window[1] < k \
                or count[2] - window[2] < k 
            ):
                window[ord(s[left])-ord("a")] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return len(s) - max_window
                
    

# Example 1:
# Input: s = "aabaaaacaabc", k = 2
# Output: 8
res = Solution2().takeCharacters(s = "aabaaaacaabc", k = 2)
print(res)

# Example 2:
# Input: s = "a", k = 1
# Output: -1
res = Solution2().takeCharacters(s = "a", k = 1)
print(res)