# GET THE DETAILS OF THE PHONE NUMBER .

# USING phonenumbers LIBRARY .

import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

# CASE ONE 

number = "+919039270900"
number = ph.parse(number)

print ( carrier.name_for_number ( number , "en" ) )
print ( geocoder.description_for_number ( number , "en" ) )
print ( timezone.time_zones_for_number ( number ) )

# CASE TWO

number = "+919039270900"
phone = ph.parse(number)

print ( carrier.name_for_number ( phone , "en" ) )
print ( geocoder.description_for_number ( phone , "en" ) )
print ( timezone.time_zones_for_number ( phone ) )