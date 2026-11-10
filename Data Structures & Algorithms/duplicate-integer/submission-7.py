class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = set()

        for i in range(len(nums)):
            if nums[i] not in contains:
                contains.add(nums[i])
            else:
                return True

        return False