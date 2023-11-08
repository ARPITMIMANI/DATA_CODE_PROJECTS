# CREATE A FIBONACCI SERIES .

# USING GENERATORS METHOD .

# DEFINE A FUNCTION .

def fibonacci():
    a = 0 
    b = 1
    while True:
        yield a 
        a , b = b , a + b

# SET THE LIMIT FOR THE FUNCTION .

# FOR THE FIBONACCI SERIES MAXIMUM LIMIT KEPT IS 100 .        

for c in fibonacci():
    if c >= 200:
        break
    print(c)

# USING while LOOP .

def fibonacci():
    a = 0 
    b = 1
    while a <= 200:
        print(a)
        a , b = b , a + b 

fibonacci()          