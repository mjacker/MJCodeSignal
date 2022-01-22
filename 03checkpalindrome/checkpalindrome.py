def solution(inputString):
    reverse = ""
    for c in inputString:
        reverse = c + reverse
    
    if reverse == inputString:
        return True
    else:
        return False

def solution2(inputString):
    return inputString == inputString[::-1]


# Main program
print("### CHECK IF IT IS A PALINDROME ###")
userInput = input("Enter a word: ")

print("Solution one: ")
if solution(userInput):
    print("\tThis word is palindrome.")
else:
    print("\tThis word is not palindrome")

print("Solution two: ")
if solution2(userInput):
    print("\tThis word is palindrome.")
else:
    print("\tThis word is not palindrome. ")
