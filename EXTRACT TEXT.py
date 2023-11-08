# EXTRACT OR COLLECT TEXT FROM THE PDF FILE .

# USING PyPDF2 LIBRARY .

import PyPDF2
from PyPDF2 import PdfReader
print ( dir(PyPDF2) )

# EXAMPLE ONE 

# CREATE A PDF READER OBJECT .

reader = PdfReader ("DEMO_TEXT.pdf")

# PRINT NUMBER OF PAGES IN PDF .

print ( len (reader.pages ) )

# GET A SPECIFIC PAGE FROM THE PDF FILE .

mypage = reader.pages[0]

# EXTRACT TEXT FROM THE PAGE .

mytext = mypage.extract_text()

# PRINT THE TEXT FROM THE PAGE .

print ( mytext )

# EXAMPLE TWO 

# CREATE A PDF READER OBJECT .

reader = PdfReader ("GOOGLE_USE_CASE.pdf")

# PRINT NUMBER OF PAGES IN PDF .

print ( len (reader.pages ) )

# GET A SPECIFIC PAGE FROM THE PDF FILE .

mypage = reader.pages[4]

# EXTRACT TEXT FROM THE PAGE .

mytext = mypage.extract_text()

# PRINT THE TEXT FROM THE PAGE .

print ( mytext )