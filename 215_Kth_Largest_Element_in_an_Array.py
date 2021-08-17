import heapq


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if(len(heap) > k):
                heapq.heappop(heap)
        return heap[0]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]