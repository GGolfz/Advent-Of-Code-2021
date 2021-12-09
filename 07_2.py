nums = input().split(',')
nums = [int(x) for x in nums]
mean = round(sum(nums) / len(nums))
sum = sum([abs(x - (mean-1))*(abs(x-(mean-1))+1)/2 for x in nums])
print(int(sum))