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
total_votes = 0
candidate_options =[]
candidate_votes = {}

winning_candidate =""
winning_count = 0
winning_percentage = 0 


with open(file_to_load) as election_data:
  #  with open(file_to_save,"w") as txt_file:
#To do: Perform Analysis
    file_reader = csv.reader(election_data)

#Printing Headers test
    headers  = next(file_reader)
    print(headers)
   
    for row in file_reader:
      candidate_name = row[2]
      if candidate_name not in candidate_options:
          candidate_options.append(candidate_name)
          candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1
      total_votes = total_votes + 1


    for candidate_name in candidate_votes: 
      votes = candidate_votes[candidate_name]
      percentage_votes = float(votes)/float(total_votes)*100
      #print(f"{candidate_name}: recieved {percentage_votes:.2f}% of the vote")
      if (votes > winning_count) and (percentage_votes > winning_percentage):
        winning_count = votes
        winning_percentage = percentage_votes 
        winning_candidate = candidate_name
      print(f"{candidate_name}: {percentage_votes:.1f}% ({votes:,})\n")

    winning_candidate_sum = (
      f"--------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"--------------------\n")
    print(winning_candidate_sum)
    
     
     
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