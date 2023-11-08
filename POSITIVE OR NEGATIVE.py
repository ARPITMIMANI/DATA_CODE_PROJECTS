# CHECK THE NUMBER IS POSITIVE , NEGATIVE OR ZERO .

# USING if elif else STATEMENT .

number = float ( input ( "ENTER THE NUMBER :" ) )

if number > 0 :
    print ( number , "IS A POSITIVE NUMBER" )

elif number < 0 :
    print ( number , "IS A NEGATIVE NUMBER" )

else :
    print ( number , "IS EQUAL TO ZERO" )    

# USING NESTED if STATEMENT .

num = float ( input ( "ENTER THE NUMBER :" ) ) 

if num >= 0 :

    if num == 0 :
        print ( num , "IS EQUAL TO ZERO" )

    else :
        print ( num, "IS A POSITIVE NUMBER" )

else :
    print ( num , "IS A NEGATIVE NUMBER" )