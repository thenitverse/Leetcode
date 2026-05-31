def is_palindrome_number(number):
    # Rule 1: Negative numbers are never palindromes (e.g., -121 != 121-)
    if number <0:
        return False
        # Rule 2: 0 is the same forward and backward
    if number == 0:
        return True
# Rule 3: Any non-zero number ending in 0 (like 10, 200) 
    # cannot be a palindrome because no integer starts with 0.
    if number != 0 and number % 10 == 0:
            return False
# We prepare to reverse the number. 
    # We store the original 'number' in 'num' because we are 
    # going to "destroy" num by dividing it until it's 0.

    rev = 0
    num = number
    while num:
        # Step A: Get the last digit using modulo 10
        # If num is 121, digit is 1
        digit = num % 10
        # Step B: Shift the 'rev' total over by one power of 10 
        # and add the new digit. 
        # If rev was 1 and digit is 2, (1 * 10) + 2 = 12.
        rev = rev*10 + digit
        # Step C: Remove the last digit from 'num' using floor division.
        # 121 // 10 becomes 12.
        num = num//10
        # Finally, check if our built 'rev' is identical to the 'number' we started with.
    return rev == number


result = is_palindrome_number(121) #true
print(result)
print(is_palindrome_number(300)) #false