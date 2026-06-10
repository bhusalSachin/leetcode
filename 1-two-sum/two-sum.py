class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        found=[]
        for i in range(0, length):
            output = []
            if nums[i] == target and target is not 0:
                found = output
                break

            for j in range(1, length):
                if j == i:
                    continue
                sum = nums[i] + nums[j]

                if sum == target:
                    output.append(i)
                    output.append(j)
                    found = output
                    break
            if found:
                break
            
        if not found:
            output = []
            for i in range(0, length):
                sum = nums[i]
                output.append(i)
                for j in range(1, length):
                    if j == i:
                        continue
                    sum = sum + nums[j]
                    output.append(j)
                    if sum == target:
                        output.append(j)
                        found = output
                        break

        return found

