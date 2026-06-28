class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=[]
        left=0
        left1=0
        while left<len(word1) and left1<len(word2):
            res.append(word1[left])
            res.append(word2[left1])
            left+=1
            left1+=1
        while left<len(word1):
            res.append(word1[left])
            left+=1
        while left1<len(word2):
            res.append(word2[left1])
            left1+=1
        return "".join(res)

            

        