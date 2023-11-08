# REVERSE A NUMBER FOR EXAMPLE THE REVERSE OF 1234 IS 4321 .

# USING while LOOP .
'''
normal_number = int ( input ( "ENTER THE NUMBER :") )
reverse_number = 0

while normal_number  != 0 :
    digit = normal_number % 10
    reverse_number = reverse_number * 10 + digit
    normal_number = normal_number // 10

print ( "THE REVERSE NUMBER IS" , reverse_number ) 
'''
# USING STRING SLICING .

normal_number = int ( input ( "ENTER THE NUMBER :") )
print ( str(normal_number) [::-1] )