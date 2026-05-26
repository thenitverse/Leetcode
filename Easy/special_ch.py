
def special_ch(word: str)->int:  #A letter is called special if it appears both in lowercase and uppercase in word.
    seen_lower = set()
    seen_upper = set()
    for ch in word:
        if ch == ch.lower():
            seen_lower.add(ch)
        elif ch == ch.upper():
            seen_upper.add(ch)
    count = 0
    for ch in seen_upper:
        if ch.lower() in seen_lower:
            count+=1
            
    return count
while True:
    user_input = input("Enter a word (or type q to quit): ")
    if user_input.lower() == "q":
        print("Goodbye!")
        break
    result = special_ch(user_input)
    print("Result: ",result)
    

    #output
    """Enter a word (or type q to quit): AAassSdfge
Result:  2
Enter a word (or type q to quit): SsNNNNnsa
Result:  2
Enter a word (or type q to quit): AABBbCCaCc
Result:  3
Enter a word (or type q to quit): q
Goodbye!"""
