#!/usr/bin/env python3

import pandas as pd
import csv

################################# Reading csv file & selecting important fields #####################################
data = pd.read_csv("Demanda_Dummytest2.csv")

# selection
df = pd.DataFrame(data, columns= ['Client','Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])

# create unique value field "Issue Type"
df["Issue Type"] = 'Demand'

# save data 
df.to_csv("df_data.csv") #, index=False)

############################## Gettting neccesary information from Jira .csv file ###################################

# Read csv
data2 = pd.read_csv("DDE.csv")

# selection
df_sumik = pd.DataFrame(data2, columns= ['Summary','Issue key'])

#################################### Issue key & Summary concatenation ##############################################
  
# Read csv
data_df = pd.read_csv("df_data.csv")

# selection
df2 = pd.DataFrame(data_df, columns= ['Issue Type', 'Client', 'Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])

# Join
result = df_sumik.join(df2, how = "outer")

# print & save data
print(result)
result.to_csv("finalData.csv")
