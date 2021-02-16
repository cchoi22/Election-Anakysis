# Retrieve Data Set
import os
os.system('cls' if os.name == 'nt' else 'clear')
import csv

import datetime as dt
# now = dt.datetime.now()
# print("The time right now is ",now)

file_to_load = os.path.join("election_results.csv")
#file_to_save= os.path.join("election_analysis.txt")

# open election file and read contents
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
  #  with open(file_to_save,"w") as txt_file:
#To do: Perform Analysis
    file_reader = csv.reader(election_data)

#Printing Headers test
    headers  = next(file_reader)
    print(headers)
    
    #for row in file_reader:
       # print(row)
#    print(election_data)
        # txt_file.write("Arapahoe, ")
        # txt_file.write("Denver, ")
        # txt_file.write("Jefferson")
# 1. Calculate the total number of votes
# 2. Get the complete list of candidates who received votes
# 3. Percentatge of votes each candidate got
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote

#close file 
# txt_file.close()