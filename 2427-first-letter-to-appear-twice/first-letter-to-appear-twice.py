class Solution:
    def repeatedCharacter(self, s: str) -> str:
        recurrings = dict()
        for i in s:
            if recurrings.get(i):
                return i    
            recurrings[i] = 1
        return None

        