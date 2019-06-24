
number= int(input("enter the number for add all digit of it: "))
sum1 = 0
for i in list(str(number)):
    sum1 += int(i)
print(sum1)
