sum = 0
n = int(input("Value for n: "))
m = n
for i in range(0, n - 1 ):
   sum += (1 + 2 * i) * 2
   print("sum: ", sum)

sum += 1 + 2 * (n - 1)  
print("sum2: ", sum)


print(sum)

"""
   For n = 4
   ---------
   1 + 2 * n

   1 + 2 * 0 = 1   
   1 + 2 * 1 = 3
   1 + 2 * 2 = 5
   1 + 2 * 3 = 7
   1 + 2 * 2 = 5
   1 + 2 * 1 = 3
   1 + 2 * 0 = 1
   --------------
   total =    25

"""