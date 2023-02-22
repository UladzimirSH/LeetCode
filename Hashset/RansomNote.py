class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = {}
        for i in magazine:
            if i in magazine_letters:
                magazine_letters[i] = magazine_letters[i] + 1
            else:
                magazine_letters[i] = 1

        for i in ransomNote:
            if i not in magazine_letters:
                return False

            magazine_letters[i] = magazine_letters[i] - 1
            if magazine_letters[i] == -1:
                return False

        return True


solution = Solution()
print(solution.canConstruct("aab", "acb"))