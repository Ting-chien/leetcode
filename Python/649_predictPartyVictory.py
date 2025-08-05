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
    

from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Use deque do handle append and insert with both O(1) in
        time complexity.

        * append(): O(1)
        * appendleft(): O(1)
        * pop(): O(1)
        * popleft(): O(1)
        """
        rad = deque()
        dir = deque()
        N = len(senate)
        # Put all senators' position to deque
        for i, s in enumerate(senate):
            if s == "R":
                rad.append(i)
            else:
                dir.append(i)
        # Compete two senators' position until one party take over
        while rad and dir:
            r = rad.popleft()
            d = dir.popleft()
            # Compare who win, senator with lower index win
            if r < d:
                rad.append(r+N)
            else:
                dir.append(d+N)

        return "Radiant" if rad else "Dire"


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