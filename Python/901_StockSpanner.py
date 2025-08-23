class StockSpanner:
    """
    Time Limit Exceed: 如果使用此操作，因為題目要求大於 10^4 次操作，
    因此越到後面時間複雜度就會越來越差。

    Complexity
    * Time: O(n^2)
    * Space: O(n)
    """

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        # Add today's price into quotes
        self.prices.append(price)
        # Count span
        span = 0
        for i in range(len(self.prices)-1, -1, -1):
            if self.prices[i] > price:
                return span
            span += 1
        return span
    
class StockSpanner:
    """
    使用 monotonic stack 來合併 price 比當天小或等於的天數

    Complexity
    * Time: O(n)
    * Space: O(n)
    """

    def __init__(self):
        self.stack = [] # 儲存 (price, span)
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price > self.stack[-1][0]:
            # 如果 price 比昨天高，則把昨日的天數合併過來
            span += self.stack.pop()[1]
        # 紀錄自己的 span 天數
        self.stack.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
ans = []
ans.append(obj.next(100))
ans.append(obj.next(80))
ans.append(obj.next(60))
ans.append(obj.next(70))
ans.append(obj.next(60))
ans.append(obj.next(75))
ans.append(obj.next(85))
print(ans)