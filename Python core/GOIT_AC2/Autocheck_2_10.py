num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    for i in range (0, num+1):
        sum += i
    num = int(input("Enter integer (0 for output): "))