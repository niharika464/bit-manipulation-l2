def numberOfBits(n):
    ones=0
    zeroes=0
    while(n):
        if (n&1 == 1):
            ones += 1
        else:
            zeroes += 1
        n >>= 1
    print("Number of ones=", ones,"\n Number of zeries=", zeroes)

number = int(input(" enter the number:"))
numberOfBits(number)       
            