# CHECK THE SPEED OF THE INTERNET .

import speedtest
print ( dir(speedtest) )
internet = speedtest.Speedtest()

# CHECK THE DOWNLOAD SPEED .

print ( "MY INTERNET DOWNLOAD SPEED :" , internet.download() )

# CHECK THE UPLOAD SPEED .

print ( "MY INTERNET UPLOAD SPEED :" , internet.upload() )