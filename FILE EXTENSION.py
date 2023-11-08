# EXTRACT EXTENSION FROM THE FILE NAME .

# USING splitext FUNCTION FROM os MODULE .

import os
print ( dir(os) )

file_extension = os.path.splitext ( 'SCREEN_TIME_APP_DETAILS.xlsx' )

print ( "THE FILE NAME WITH EXTENSION IS" , file_extension )
print ( "THE FILE NAME IS" , file_extension[0] )
print ( "THE EXTENSION OF FILE IS" , file_extension[1] )

# USING pathlib MODULE .

import pathlib
print ( dir(pathlib) )

print ( pathlib.Path ('SCREEN_TIME_APP_DETAILS.xlsx') .suffix )