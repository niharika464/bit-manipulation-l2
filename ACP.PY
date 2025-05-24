def number(n):
    count = 0
    while n:
        count += 1
        n <<= 1
        print(count, "count the loops")
n=int(input("Enter the number:"))
number(n)        