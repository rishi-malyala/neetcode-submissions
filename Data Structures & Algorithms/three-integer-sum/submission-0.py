class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []

        for p1 in range(len(nums) - 2):

            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue

            p2 = p1 + 1
            p3 = len(nums) - 1

            while p2 < p3:

                sumd = nums[p1] + nums[p2] + nums[p3]

                if sumd == 0:
                    sums.append([nums[p1], nums[p2], nums[p3]])

                    p2 += 1
                    p3 -= 1

                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1

                    while p2 < p3 and nums[p3] == nums[p3 + 1]:
                        p3 -= 1

                elif sumd > 0:
                    p3 -= 1

                else:
                    p2 += 1

        return sums