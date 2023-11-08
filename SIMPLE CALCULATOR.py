# CREATE A SIMPLE CALCULATOR WHICH CAN DO ADDITION , SUBSTRACTION , MULTIPLICATION , FLOAT DIVISION , FLOOR DIVISION , MODULUS , EXPONENTIATION  OF TWO NUMBERS GIVEN BY USER .

calculation = input ( "INTERESTED IN DOING CALCULATION :" )

no_calculation = [ "NO" , "False" , "FALSE" , "NOT" , "FAIL", "No" , "no" , "fail" , "false" , "Not" , "Fail" ,"not" ]

if calculation in no_calculation :
    pass

else:

    num1 = float ( input ( "ENTER THE FIRST NUMBER :" ) )
    num2 = float ( input ( "ENTER THE SECOND NUMBER :" ) )
    operator = input ( "ENTER THE OPERATOR :" )

    if operator == "+" :
        print ( "THE OUTPUT IS" , num1 + num2 )

    elif operator == "-" :
        print ( "THE OUTPUT IS" , num1 - num2 )    

    elif operator == "*" :
        print ( "THE OUTPUT IS" , num1 * num2 ) 

    elif operator == "/" :
        print ( "THE OUTPUT IS" , num1 / num2 )

    elif operator == "//" :
        print ( "THE OUTPUT IS" , num1 // num2 )      

    elif operator == "%" :
        print ( "THE OUTPUT IS" , num1 % num2 )

    elif operator == "**" :
        print ( "THE OUTPUT IS" , num1 ** num2 ) 

    else:
        print ( "OPERATOR IS INVALID" ) 