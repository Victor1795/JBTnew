 #!/usr/bin/env python3

import pandas as pd
import csv
import numpy as np
#from pandas.testing import assert_frame_equal



################################# NEW EPIC / WHERE YOU NEED TO COMPARE FIRST TO SEE IF IT EXISTS  #####################################
######### requeriments: 
##### 1 compare Client(Dummy) vs Summary(Jirav) // COMPARA
####  2 If not found (false) define Issue Type as Epic(newCSV) // IF
####  3 Use Client(Dummy) as Summary(newCSV) // COMPARA 
####  4 set Status OPEN(newCSV) // #3 es condicional 


# new csv is newcsv

######## read / bring over
# dummy_data.csv
# global_data.csv
data1 = pd.read_csv('dummy_data.csv')#,sep="\s+")
data2 = pd.read_csv('global_data.csv')#,sep="\s+")

###### compare roleID vs Summary
df1 = pd.DataFrame(data1, columns=['Client'])


df2 = pd.DataFrame(data2, columns=['Summary'])


result = df1.join(df2, how = "outer")

#print(result)

## create new column to check. true= theyre already a subtask, false means we need to add them as new ones and use the ID as summary
#print(result) # nuevo dataframe



# to show the fields that are important to you
df = pd.DataFrame(columns= ['Epic Name','Summary','Issue Type','Status'])



i = 0
#print(i)
# iteration starts 
# Iterating using while loop
while i < result['Client'].count():
    x = result.loc[i,'Client']
    y = 'Epic'
    z = 'OPEN'
    #print(i)
    #print(x)
    boolean_finding = result['Summary'].str.contains(x).any()

    if(boolean_finding == False ):
    # to show the fields that are important to you
        v = [x,x,y,z]
        v1 = pd.Series(v, index = df.columns)
        #print(v)
        df = df.append(v1, ignore_index=True)
        #print(df)
        #df.to_csv("epic_data.csv")
        s = [np.nan,x]
        s1 = pd.Series(s, index = result.columns)
        result = result.append(s1, ignore_index=True)
        df.to_csv("epic_data.csv", index=False)
# Find string in summary columns
        #print(df)
        #print(result)

# Returns true if the
        #print(boolean_finding)

#Outpu 
#True se hace automaticamente un subtask, false se crea constante issue type como epic 

    i = i + 1 # close while


print(df)
