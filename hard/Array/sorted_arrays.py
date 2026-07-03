def find_median_sorted_arrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    if m > n:
        return find_median_sorted_arrays(nums2,nums1)

    total_len = m + n
    half = (m + n)//2
    left = 0
    right = m
    while left<=right:
        mid1 = (left+right)//2
        mid2 = half - mid1
        if mid1 > 0:
            left_one = nums1[mid1 - 1]
        else:
            left_one = float("-inf")
        if mid1 == m:
            right_one = float("inf")
        else:
            right_one = nums1[mid1]
        if mid2 == 0:
            left_two = float("-inf")
        else:
            left_two = nums2[mid2 - 1]
        if mid2 == n:
            right_two = float("inf")
        else:
            right_two = nums2[mid2]
        if left_one <= right_two and left_two <= right_one:
            if total_len % 2 != 0:
                median = min(right_one,right_two)
                return float(median)
            if total_len % 2 == 0:
                
                median = (max(left_one,left_two) + min(right_one,right_two)) /2
                return median
        
        if left_one > right_two:
            right = mid1 - 1
        else:
            left = mid1 + 1
            
print(find_median_sorted_arrays([1, 3], [2]))        # 2.0
print(find_median_sorted_arrays([1, 2], [3, 4]))     # 2.5
print(find_median_sorted_arrays([], [5]))            # 5.0
print(find_median_sorted_arrays([1], [2, 3, 4, 5, 6]))  # 3.5
      
            
            
            
        
    
