# FIND THE LARGEST OF THREE NUMBERS .

num1 = float ( input ( "ENTER THE FIRST NUMBER :") )
num2 = float ( input ( "ENTER THE SECOND NUMBER :") )
num3 = float ( input ( "ENTER THE THIRD NUMBER :") )

if ( num1 >= num2 )and ( num1 >= num3 ) :
    largest = num1

elif ( num2 >= num1 )and ( num2 >= num3 ) :
    largest = num2

else :
    largest = num3

print ( "THE LARGEST NUMBER IS" , largest )