class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        low = 0
        hi = length - 1

        while(low<=hi):
            mid = low + (hi - low)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid-1
            else:
                low = mid+1
        return -1
