numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 21, 27, 51,]

prime = []

for i in numbers:
    if i != 1:
        for x in range(2, i):
            if i % x == 0:
                break 
        else:
            prime.append(i)
        
    else:
        prime.append(i)

print(prime)



