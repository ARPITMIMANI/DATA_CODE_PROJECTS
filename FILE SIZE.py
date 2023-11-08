# CHECK THE FILE SIZE .

# USING THE os MODULE .

import os
print ( dir(os) )

file_size = os.stat ('SCREEN_TIME_APP_DETAILS.xlsx')
print ( file_size.st_size )

# THE OUTPUT WILL BE ALWAYS IN BYTE .

# USING pathlib MODULE .

from pathlib import Path

file_size = Path ('SCREEN_TIME_APP_DETAILS.xlsx')
print ( file_size.stat().st_size )

# THE OUTPUT WILL BE ALWAYS IN BYTE .