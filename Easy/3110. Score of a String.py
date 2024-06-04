#3110. Score of a String

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for position in range(len(s)-1):
            score = score + abs( 
                ord(s[position]) -
                ord(s[position + 1]))
        return score

Solution_Instance = Solution()