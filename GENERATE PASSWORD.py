# GENERATE A RANDOM PASSWORD OF SPECIFIC LENGTH .

# PASSWORD CAN CONSIST OF UPPERCASE ALPHABETS , LOWERCASE ALPHABETS , NUMBERS AND SPECIAL CHARACTERS .

import random
print ( dir(random) )

password_length = int ( input ( "ENTER THE LENGTH OF PASSWORD TO BE GENERATED :") )
characters_list = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!@#$%&?:;|/\=+-~*^"
password = "".join ( random.sample ( characters_list , password_length ) )
print (password)