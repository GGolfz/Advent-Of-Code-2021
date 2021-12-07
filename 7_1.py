nums = input().split(',')
nums = [int(x) for x in nums]
nums.sort()
med = nums[len(nums)//2]
print(med)
sum = sum([abs(x-med) for x in nums])
print(sum)