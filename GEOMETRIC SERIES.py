# PRINT THE SERIES 1 , 3 , 9 , 27 , 81 , 243 , 729 , 2187 , ... AND SO ON .

# USING while LOOP .

def num():
    a = 1
    b = 3
    while a <= 20000:
        print(a)
        a = b
        b = 3 * b
num() 

# USING GENERATORS METHOD .

def num():
    a = 1
    b = 3
    while True:
        yield a
        a = b
        b = 3 * b

for c in num():
    if c >= 20000 :
        break
    print(c)