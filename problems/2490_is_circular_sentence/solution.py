class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        sentence = sentence.split(" ")

        n = len(sentence)
        
        if n == 1:
            return sentence[0][0] == sentence[0][-1]
        
        for i in range(1, n):
            if sentence[i][0] != sentence[i-1][-1]:
                return False
            if i == n-1:
                if sentence[i][-1] != sentence[0][0]:
                    return False
        return True
            