class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1=set(ransomNote)
        for ch in s1:
            if ransomNote.count(ch)>magazine.count(ch):
                return False
    
        return True
