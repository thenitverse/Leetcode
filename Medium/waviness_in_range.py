def waviness_in_range(num1,num2):
    total = 0
    for x in range(num1,num2 + 1): # it will give all numbers from num1 to num2 including both indices 0 and last one[num1,num2]
        s = str(x)
        for i in range(1,len(s) - 1):  # here we are skipping first and last index 
            if ((s[i] < s[i - 1] and s[i] < s[i+1]) or (s[i] > s[i-1] and s[i] > s[i+1])):
                total+=1

    return total


num1 = 121
num2 = 323
result = waviness_in_range(num1,num2)
print(result)

print(waviness_in_range(121,125))