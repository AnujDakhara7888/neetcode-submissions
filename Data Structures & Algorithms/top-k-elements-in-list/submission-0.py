import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1
        queue = []
        for num,freq in count.items():
            heapq.heappush(queue,(freq,num))

            if len(queue)>k:
                heapq.heappop(queue)

        result = []
        while queue:
            freq,num = heapq.heappop(queue)
            result.append(num)

        return result

        