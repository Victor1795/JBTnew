#!/usr/bin/env python3
  
import pandas as pd
import csv

################################# Reading Jira csv file & selecting important fields ##################################

data = pd.read_csv("TODOS.csv")

# selection
df = pd.DataFrame(data, columns= ['Summary','Issue key','Issue id','Parent id','Issue Type','Status','Custom field (POC JBT)','Custom field (IQN)','Custom field (Client JBT)','Custom field (Project JBT)','Custom field (Role Title)','Custom field (Role Id)','Custom field (Resource Start Date)','Custom field (Role Created)','Custom field (Resource End Date)'])

# save data 
df.to_csv("global_data.csv", index=False)

############################## Reading DummyHR csv file & selecting important fields ###################################

data = pd.read_csv("Demanda_DummyCOMPARING.csv")

# selection
df = pd.DataFrame(data, columns= ['Client','Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])

# save data
df.to_csv("dummy_data.csv", index=False)


########################### reading only epic csv with imp fields ###########
data = pd.read_csv("NEW_TODOS.csv")

# selection
df = pd.DataFrame(data, columns= ['Summary', 'Issue key', 'Issue id', 'Parent id', 'Issue Type', 'Status'])

# save data
df.to_csv("new_global_data.csv", index=False)
