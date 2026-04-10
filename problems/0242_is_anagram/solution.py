class Solution1:
    '''
    Use a map to store appeared chars
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        s_dict, t_dict = self.get_dict(s), self.get_dict(t)
        for k, v in sorted(s_dict.items()):
            if not (k in t_dict and t_dict[k] == v):
                return False
        return True

    def get_dict(self, str):
        d = {}
        for char in str:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        return d

class Solution2:
    '''
    Sort two string and compare if they are identical
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution3:
    '''
    Use array with 26 space to save chars values
    '''
    def isAnagram(self, s: str, t: str) -> bool:

        s_arr, t_arr = self.count_by_array(s), self.count_by_array(t)

        for i in range(26):
            if not s_arr[i] == t_arr[i]:
                return False

        return True


    def count_by_array(self, str):
        available = [0]*26
        for char in str:
            index = ord(char) - 97
            available[index] += 1
        return available
        

if __name__ == '__main__':
    sol = Solution3()
    ans1 = sol.isAnagram("anagram", "nagaram")
    print(f'ans1={ans1}')
    ans2 = sol.isAnagram("rat", "car")
    print(f'ans2={ans2}')