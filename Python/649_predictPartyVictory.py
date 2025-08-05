class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Time: 18mins
        Performance: 
        * Time Beats 5.01% 👎🏻
        * Space beats 98%
        """
        
        senators = list(senate)

        # If not all senators from the same party, keep voting
        while len(set(senators)) > 1:
            s = senators.pop(0)
            if s == "R":
                senators.remove("D")
            if s == "D":
                senators.remove("R")    
            senators.append(s)

        return "Radiant" if set(senators).pop() == "R" else "Dire"

# Example 1:
# Input: senate = "RD"
# Output: "Radiant"
res = Solution().predictPartyVictory(senate = "RD")
print(res)

# Example 2:
# Input: senate = "RDD"
# Output: "Dire"
res = Solution().predictPartyVictory(senate = "RDD")
print(res)