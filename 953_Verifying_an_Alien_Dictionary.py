from _ast import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j == len(words[i + 1]):
                    return False
                idx1 = dic[words[i][j]]
                idx2 = dic[words[i + 1][j]]
                if idx1 > idx2:
                    return False
                if idx1 < idx2:
                    break
        return True
