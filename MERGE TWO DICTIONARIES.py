# MERGE THE TWO DICTIONARIES .

# USING " | " OPERATOR .

dict1 = { "GEOGRAPHY":88 , "ENGLISH":76 , "HISTORY":64 , "ECONOMICS":60 }
dict2 = {"MATHS":92 , "PHYSICS":72 , "CHEMISTRY":80 , "BIOLOGY":56 }

newdict = dict1 | dict2
print(newdict)

# USING copy AND update FUNCTIONS .

dict1 = { "GEOGRAPHY":88 , "ENGLISH":76 , "HISTORY":64 , "ECONOMICS":60 }
dict2 = {"MATHS":92 , "PHYSICS":72 , "CHEMISTRY":80 , 
"BIOLOGY":56 }

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

# USING ONLY update FUNCTIONS .

dict1 = { "GEOGRAPHY":88 , "ENGLISH":76 , "HISTORY":64 , "ECONOMICS":60 }
dict2 = {"MATHS":92 , "PHYSICS":72 , "CHEMISTRY":80 , 
"BIOLOGY":56 }

dict1.update(dict2)
print(dict1)