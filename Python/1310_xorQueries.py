from typing import List


class Solution1:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for q in queries:
            l_p, r_p = q[0], q[1]
            count = 0
            for i in arr[l_p:r_p+1]:
                count ^= i
            res.append(count)
        return res

class Solution2:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # generate a list of prefix xor
        p_xor = [0]*(len(arr)+1)
        for i in range(len(arr)):
            p_xor[i+1] = p_xor[i] ^ arr[i]
        # for each query q, compute the XOR from q[0] to q[1]+1
        # which is equal to XOR between p_xor[q[1]+1] and p_xor[q[0]]
        res = []
        for q in queries:
            l_p, r_p = q[0], q[1]
            res.append(p_xor[r_p+1]^p_xor[l_p])
        return res
    

if __name__ == "__main__":

    # Example 1
    # Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
    # Output: [2,7,14,8] 
    print(Solution2().xorQueries(arr=[1,3,4,8], queries=[[0,1],[1,2],[0,3],[3,3]]))

    # Example 2
    # Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
    # Output: [8,0,4,4]
    print(Solution2().xorQueries(arr=[4,8,2,10], queries=[[2,3],[1,3],[0,0],[0,3]]))

    # Example 2
    # Input: arr = [1,11,1], queries = [[0,2],[0,2],[2,2],[0,2]]
    # Output: [11,11,1,11]
    print(Solution2().xorQueries(arr=[1,11,1], queries=[[0,2],[0,2],[2,2],[0,2]]))
