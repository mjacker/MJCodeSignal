from random import random


def solution(inputArray):
    maxProduct = inputArray[0] * inputArray[1]
    i = 0
    while i < len(inputArray) - 1:
        if maxProduct < inputArray[i] * inputArray[i + 1]:
            maxProduct = inputArray[i] * inputArray[i + 1]
        i = i + 1
    return maxProduct       

myArray = [3, 6, -2, -5, 7, 3]

print("Your input array is: ", myArray)
print("The max Adjacent Product is: ", solution(myArray))