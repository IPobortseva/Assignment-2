"""
task 1, it prints my variable
"""
H = ("Hello, Python World!")
print (H)
"""
task 2, does mathematical operations
"""
a = int (input())
b = int (input())
print (a + b, a - b, a * b, a / b)

"""
#task 3
"""
c = ("горіх")
d = ("котик")
words = c + " " + d
print (words)
print (len (words))

"""
#task 4
"""
n = int(input())
if n%2 == 0:
    print ("Парне")
else:
    print ("Непарне")

"""
#task 5
"""
for i in range (1, 11):
    print(i)
"""
#task 6
"""
num = int(input())
if num > 0:
    print ("Позитивний")
elif num ==0:
    print ("Нуль")
else:
    print ("Негативний")

"""
Task 7
"""
for i in range (2, 11, 2):
    print (i)

"""
task 8
"""
a = int(input())
total = 0
for i in range (1, a+1):
    total +=i
    print (total)

"""
task 9
"""
for i in range (10, 0 , -1):
    print (i)

"""
task 10
"""
for i in range (1,10):
    if i == 5:
        continue
    if i == 7:
        break
    print (i)