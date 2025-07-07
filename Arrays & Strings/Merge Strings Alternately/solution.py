class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j, k = 0, 0, 0

        while i<len(word1) and j<len(word2):
            if k%2:
                result.append(word2[j])
                j+=1
            else:
                result.append(word1[i])
                i+=1
            k+=1
        
        for i in range(i, len(word1)):
            result.append(word1[i])

        for j in range(j, len(word2)):
            result.append(word2[j])

        return "".join(result)