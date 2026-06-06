def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        width = right - left # (right - left) is the width (the distance between the two pointers).
        length = min(height[left],height[right])
        area = length * width
        max_water = max(max_water, area) #    max() compares this new area with the previous max_water and keeps the larger of the two.


        if height[left] < height[right]:
            left +=1  #If the left line is shorter, we move left to the right (+1).
        else:
            right -=1 #If the right line is shorter (or they are equal), we move right to the left (-1).

    return max_water

height = list(map(int,input("Enter list of hights: ").split(",")))
result = max_area(height)
print("output: ",result)

"""output:
Enter list of hights: 1,2,3,4,5,6,7,8
output:  16"""