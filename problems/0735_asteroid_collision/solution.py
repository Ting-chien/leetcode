from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Use a stack to store asteroids with the same sign(direction).
        Once we met a different sign asteroid, it will compete size with
        asteroids in stack from the tail.
        
        For asteroids[i] and stack[j]
            If asteroids[i] > stack[j], remove stack[j]
                if len(stack) > 0, compete again
                else add asteroids[i] to stack
            elif asteroids[i] < stack[j], remove asteroids[i]
            else asteroids[i] == stack[j], asteroids[i] and stack[j]
                
        """
        stack = []
        for curr in asteroids:
            if stack:
                # compete two asteroids
                if curr * stack[-1] > 0:
                    # Same sign, add to stack
                    stack.append(curr)
                else:
                    # Different sign, compete
                    prev = stack.pop()
                    while prev:
                        # Current aestroid is smaller, collided
                        if abs(prev) > abs(curr):
                            stack.append(prev)
                            prev = None
                        # Both aestroid are the same, both collided
                        elif abs(prev) == abs(curr):
                            prev = None
                        # Existed aestroid is smaller, collided and try next
                        else:
                            prev = stack.pop() if stack else None
                            if not prev:
                                stack.append(curr)
            else:
                stack.append(curr)
        return stack
    

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        I missunderstand the problem in solution 1, in this problem
        only two asteroids moving right and left will collide. Hence,
        we have few condition,

        1. If asteroids[i] > 0, move to stack
        2. If asteroids[i] < 0, 
            2-1. If no positive sign asteroid in stack, move to stack
            2-2. Compete stack[-1] and asteroids[i]
                2-2-1. If the same, explode
                2-2-2. stack[-1] > asteroids[i], break
                2-2-3. stack[-1] < asteroids[i], compete again
        """
        stack = []
        for a in asteroids:
            # Only there are positive aestroids in stack and a < 0
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    # left sign aestroid size bigger
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    # same size
                    stack.pop()
                # left sign aestroid size smaller
                break
            else:
                stack.append(a)

        return stack

    

# # Example 1:
# # Input: asteroids = [5,10,-5]
# # Output: [5,10]
# res = Solution().asteroidCollision(asteroids = [5,10,-5])
# print(res)

# # Example 2:
# # Input: asteroids = [8,-8]
# # Output: []
# res = Solution().asteroidCollision(asteroids = [8,-8])
# print(res)

# # Example 3:
# # Input: asteroids = [10,2,-5]
# # Output: [10]
# res = Solution().asteroidCollision(asteroids = [10,2,-5])
# print(res)

# Example 4:
# Input: asteroids = [-2,-1,1,2]
# Output: [-2,-1,1,2]
res = Solution().asteroidCollision(asteroids = [-2,-1,1,2])
print(res)
