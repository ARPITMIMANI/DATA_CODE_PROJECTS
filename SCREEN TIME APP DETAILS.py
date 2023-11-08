# SCREEN TIME ANALYSIS IS THE TASK OF ANALYZING AND CREATING A REPORT ON WHICH APPLICATIONS AND WEBSITES ARE USED BY THE USER FOR HOW MUCH TIME. 

# APPLE DEVICES HAVE ONE OF THE BEST WAYS OF CREATING A SCREEN TIME REPORT.

import pandas as pd
import numpy as np
import plotly.express as ex
import plotly.graph_objects as go

# LOAD THE COMPLETE CSV FILE .

df = pd.read_csv("SCREEN_TIME_APP_DETAILS.csv")
print( df.to_string() )

# CHECK THE NULL VALUES IN THE DATA SET .

print ( df.isnull().sum() )

# CHECK THE STATISTICS OF DATA SET .

print ( df.describe() )

# CHECK THE INFORMATION OF DATA SET .

print ( df.info() )

# DISPLAY THE LIST OF COLUMNS OF DATA SET .

print ( df.columns )

# CREATE A BAR PLOT OF COLUMN "Date" VS COLUMN "Usage" USING plotly .

f1 = ex.bar ( data_frame=df , x="Date" , y="Usage" , color="App" , title="DATE VS USAGE" )
f1.show()

# CREATE A BAR PLOT OF COLUMN "Date" VS COLUMN "Notifications" USING plotly .

f2 = ex.bar ( data_frame=df , x="Date" , y="Notifications" , color="App" , title="DATE VS NOTIFICATIONS" )
f2.show()

# CREATE A BAR PLOT OF COLUMN "Date" VS COLUMN "Times_Opened" USING plotly .

f3 = ex.bar ( data_frame=df , x="Date" , y="Times_Opened" , color="App" , title="DATE VS TIMES OPENED" )
f3.show()

# CREATE A SCATTER PLOT OF COLUMN "Notifications" VS COLUMN "Usage" USING plotly .

f4 = ex.scatter ( data_frame=df , x="Notifications" , y="Usage" , size="Notifications" ,  trendline="ols" , title="RELATIONSHIP BETWEEN NUMBER OF NOTIFICATIONS AND AMOUNT OF USAGE" )
f4.show()