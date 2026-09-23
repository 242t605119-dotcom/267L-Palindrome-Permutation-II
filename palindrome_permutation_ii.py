class Solution:
    def generatePalindromes(self, s):
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        odd_chars = [char for char in counts if counts[char] % 2 == 1]

        if len(odd_chars) > 1:
            return []

        middle = odd_chars[0] if odd_chars else ""

        half = []

        for char in sorted(counts):
            half.extend([char] * (counts[char] // 2))

        result = []
        used = [False] * len(half)

        def backtrack(path):
            if len(path) == len(half):
                left = "".join(path)
                result.append(left + middle + left[::-1])
                return

            for i in range(len(half)):
                if used[i]:
                    continue

                if i > 0 and half[i] == half[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(half[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])

        return result
