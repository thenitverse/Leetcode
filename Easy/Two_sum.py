def two_swm(nums:list[int],target:int)->list[int]:
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

nums = list(map(int,input("Enter numbers separated by ',' :").split(',')))

target = int(input("Enter a target number: "))    
result = two_swm(nums,target)
print(result)


"""output:
Enter numbers separated by ',' :3,4,5,6
Enter a target number: 9
[0, 3]
"""