class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_n = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    list_n.append(i)
                    list_n.append(j)
                    list_n.sort()
                    return list_n