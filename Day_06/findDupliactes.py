def findDuplicates(nums):
        duplicate_numbers = []
        for i in nums:
            i = abs(i)
            
            if nums[i - 1] > 0:
                nums[i - 1] *= -1
            else:
                duplicate_numbers.append(i)
        
        print(duplicate_numbers)
    

n=int(input())
nums=[]
for i in range(n):
    num=int(input().strip())
    nums.append(num)
result=findDuplicates(nums)