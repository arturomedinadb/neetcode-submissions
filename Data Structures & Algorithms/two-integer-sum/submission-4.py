class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_s = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] + nums[i] == target and i !=j:
                    list_s.append(i)
                    list_s.append(j)
        return sorted(set(list_s))

        # for i in range(len(nums)-1):
        #     list_s = []
        #     nums = sorted(nums)
        #     if nums[i] + nums[i+1] == target and i != i+1:
        #         list_s.append(i)
        #         list_s.append(i+1)
        #     return sorted(list_s)
