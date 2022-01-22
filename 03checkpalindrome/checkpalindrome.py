def solution(inputString):
    reverse = ""
    for c in inputString:
        reverse = c + reverse
    
    if reverse == inputString:
        return True
    else:
        return False

if solution(input("Enter a word, I will check if it is palindrome: ")):
    print("This word is palindrome.")
else:
    print("This word is not palindrome")
