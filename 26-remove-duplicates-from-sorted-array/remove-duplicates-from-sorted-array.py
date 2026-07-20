class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        enums = nums.copy()
        length = len(enums)
        for idx in range(length - 1):
            # print(idx, k, nums)
            if nums[idx-k] == '_':
                break
            elif enums[idx] == enums[idx+1]:
                nums.pop(idx-k)
                nums.append('_')
                k += 1
        
        return len(enums) - k
