# Outputs: 
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
import csv
import os

# Direct path
# Assign a variable to load a file from a path.
file_to_load="Resources/election_results.csv"
# Indirect Path
# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")

# Initialize parameters
total_votes=0

candidate_options=[]
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file
with open(file_to_load) as election_data:
    ###### To do: read and analyze the data here ######

    # Read the file object with the reader function
    file_reader=csv.reader(election_data)
    
    # Reader the header (skip first row)
    headers=next(file_reader)
   
    for row in file_reader:
        # Add to the total vote count.
        total_votes+=1
        candidate_name=row[2]

        # If the candidate does not match any existing candidate, add it to the list of candidates.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        # add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
    
    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage=votes/total_votes*100
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if votes>winning_count and vote_percentage>winning_percentage:
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
    
    winning_candidate_summary=(
        f"-------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


#with open(file_to_save,"w") as txt_file:
    # write some data to the file
#    txt_file.write("Counties in the Election\n------------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")