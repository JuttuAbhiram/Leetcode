class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            count=num.count(str(i))
            if count!=int(num[i]):
                return False
        return True