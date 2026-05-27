def thre_summ(nums):
    nums.sort()
    result = []
    for i in range(len(nums)-2): # -2 for two pointers left and right
        
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums)-1
        while left < right:
            total = nums[i] + nums[left] +nums[right]
            if total == 0:
                result.append([nums[i],nums[left],nums[right]])
                left +=1
                right-=1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -=1

            elif total < 0:
                left +=1
            else:
                right -=1
    return result

nums = list(map(int,input("Enter the numbers separated by comma: ").split(',')))
result = thre_summ(nums)
print("result: ",result)

"""output:
Enter the numbers separated by comma: -2,0,2,1,0,1,1,1
result:  [[-2, 0, 2], [-2, 1, 1]]"""
