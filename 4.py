def get_digit(number, n):
    return number // 10**n % 10

max=0

for i in range(500,1000):
    for j in range(500,1000):
        if get_digit(i*j,0)==get_digit(i*j,5) and get_digit(i*j,1)==get_digit(i*j,4) and get_digit(i*j,2)==get_digit(i*j,3):
            if i*j>max:
                max=i*j

print max

#906609
