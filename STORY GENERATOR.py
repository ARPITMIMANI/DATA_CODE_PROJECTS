# GENERATE A RANDOM STORY EVERY TIME THE USER RUNS THE PROGRAM .

# USING random MODULE .

import random
# print ( dir(random) )

# STORE THE PARTS OF THE STORIES IN DIFFERENT LIST .

when = [ "FEW DAYS AGO" , "SIX WEEK AGO" , "FOUR MONTH AGO" , "ONE YEAR AGO" , "TEN HOURS BEFORE" , "A FORT NIGHT AGO" , "LAST NIGHT" , "A DAY BEFORE YESTERDAY" ]

who = [ "A BOY" , "A GARDENER" , "A PLUMBER" , "AN ELECTRICIAN" , "A MAN" , "A CARPENTER" , "A STUDENT" ]

name = [ "TOM" , "JIM" , "LEO" , "DAX" , "SAM" , "BOB" , "REX" , "ASH" , "NIC" , "REX" ]

country = [ "NORWAY" , "ICELAND" , "SWEDEN" , "FINLAND" , "IRELAND" , "SCOTLAND" , "WALES" , "ENGLAND" , "GREENLAND" , "DENMARK" ]

where = [ "FOREST" , "LAKE SIDE" , "GARDEN" , "BEACH" , "ZOO"  , "RIVER SIDE" , "NATIONAL PARK" , "HILL STATION" , "ISLAND" ]

happened = [ "FOUND A KEY" , "WROTE A BOOK" , "WATCHED BIRDS" , "READ A NEWSPAPPER" , "FOUND AN OLD COIN" , "PLAYED CHESS" , "WATCHED SUNSET" , "ATE PIZZA" , "SOLVED PUZZLES" , "DRANK ORANGE JUICE" , "ATE APPLE" , "WATCHED A MOVIE" , "MADE A VIDEO" , "TOOK PHOTOS" ]

# SELECT THR RANDOM PARTS OF THE STORY STORED IN DIFFERENT LIST USING random MODULE .

print ( random.choice(when) , random.choice(who) , "NAMED" , random.choice(name) , "LIVED IN" , random.choice(country) , "WENT TO THE" , random.choice(where) , "AND" , random.choice(happened) , "." )