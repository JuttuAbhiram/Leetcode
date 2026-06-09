class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for ch in s:
            if ch.isalnum():
                cleaned+=ch.lower()
        left=0
        right=len(cleaned)-1
        while right>=left:
            if cleaned[right]==cleaned[left]:
                right-=1
                left+=1
            else:
                return False
        return True

        