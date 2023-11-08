# GENERATE QR CODE OF ANY GIVEN LINK .

# USING pyqrcode LIBRARY .

import pyqrcode
from pyqrcode import QRCode
print ( dir(pyqrcode) )

# CASE ONE 

link = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
qr_code = pyqrcode.create(link)
qr_code.svg ( "MY_QR_CODE.svg" , scale=12 )

# CASE TWO 

link = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
qr_code = pyqrcode.create(link)
qr_code.svg ( "MY_QR_CODE.html" , scale=12 )