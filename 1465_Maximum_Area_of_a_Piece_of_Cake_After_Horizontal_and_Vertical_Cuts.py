class Solution1:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        length = horizontalCuts[0]
        height = verticalCuts[0]

        for i in range(1, len(horizontalCuts)):
            length = max(length, horizontalCuts[i] - horizontalCuts[i - 1])
        length = max(length, h - horizontalCuts[-1])

        for i in range(1, len(verticalCuts)):
            height = max(height, verticalCuts[i] - verticalCuts[i - 1])
        height = max(height, w - verticalCuts[-1])

        return length * height % (10 ** 9 + 7)


class Solution2:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        return self.getMax(h, horizontalCuts) * self.getMax(w, verticalCuts) % (10 ** 9 + 7)

    def getMax(self, last, arr):
        arr.sort()
        ret = arr[0]
        for i in range(1, len(arr)):
            ret = max(ret, arr[i] - arr[i - 1])
        return max(ret, last - arr[-1])


class Solution3:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalStrips = [0] + sorted(horizontalCuts) + [h]
        verticalStrips = [0] + sorted(verticalCuts) + [w]

        maxStripWidth = max([horizontalStrips[i + 1] - horizontalStrips[i] for i in range(len(horizontalStrips) - 1)])
        maxStripHeight = max([verticalStrips[i + 1] - verticalStrips[i] for i in range(len(verticalStrips) - 1)])

        return (maxStripWidth * maxStripHeight) % ((10 ** 9) + 7)