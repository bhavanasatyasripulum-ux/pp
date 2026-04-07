n=int(input("how many numbers? "))
total = 0
for i in range(n):
    num = int(input("enter number: "))
    total += num
    print("running total:",total)
