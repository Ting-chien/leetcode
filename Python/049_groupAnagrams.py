from typing import List

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in d:
                d[sorted_str].append(str)
            else:
                d[sorted_str] = [str]
        return list(d.values())

if __name__ == '__main__':
    sol = Solution1()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))