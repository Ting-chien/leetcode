import heapq

class SmallestInfiniteSet:
    """
    Use a min heap to store num add by user, and another variable
    curr to act as infinite set.

    Approach
    1. For popSmallest(), return current value if there is no element
    in min heap or current is smaller than m_heap[0]
    2. For addBack(), add new value if num is smaller than current value,
    and not in heap

    Complexity
    * Time: O(nlogn) - beats 74.57%
    * Space: O(nlogn) - beats 82.58%
    """

    def __init__(self):
        self.m_heap = []
        self.curr = 0
        

    def popSmallest(self) -> int:
        if self.m_heap and self.m_heap[0] <= self.curr:
            return heapq.heappop(self.m_heap)
        else:
            self.curr += 1
            return self.curr
        

    def addBack(self, num: int) -> None:
        if num <= self.curr and num not in self.m_heap:
            heapq.heappush(self.m_heap, num)


smallest_infinite_set = SmallestInfiniteSet()
print(smallest_infinite_set.popSmallest())
print(smallest_infinite_set.addBack(1))
print(smallest_infinite_set.popSmallest())
print(smallest_infinite_set.popSmallest())
print(smallest_infinite_set.popSmallest())
print(smallest_infinite_set.addBack(2))
print(smallest_infinite_set.addBack(3))
print(smallest_infinite_set.popSmallest())
print(smallest_infinite_set.popSmallest())