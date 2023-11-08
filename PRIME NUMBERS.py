# ENTER THE LIST OF PRIME NUMBERS STARTING FROM A PARTICULAR NUMBER TO ENDING FROM A PARTICULAR NUMBER .

# USING for LOOP AND if elif else STATEMENT .

num1 = int ( input ( "ENTER THE FIRST NUMBER :" ) )
num2 = int ( input ( "ENTER THE SECOND NUMBER :" ) )

if num1 < num2 :

    for x in range ( num1 , num2 + 1 ) :
        for y in range ( 2 , num2 + 1 ) :
            if x % y == 0 :
                break
        if x == y :
            print ( x , end="," )

else :
    print ( "INVALID NUMBERS" ) 