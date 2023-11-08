# TO CREATE AGE CALCULATOR IT REQUIRES TWO THINGS "TODAYS DATE" AND "DATE OF BIRTH" ONLY .

import datetime
print ( dir(datetime) )

def myage ( YEAR , MONTH , DATE ) :

    todaysdate = datetime.datetime.now().date()
    birthdate = datetime.date ( YEAR , MONTH , DATE)
    age = int ( ( todaysdate - birthdate ).days/365.25 )
    print(age)

print ( myage ( 1996 , 1 , 12 ) )