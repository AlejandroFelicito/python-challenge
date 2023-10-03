import csv
import os

input_path = os.path.join('.', 'Resources', 'election_data.csv')
output_path = os.path.join('.', 'analysis', 'results.txt')

original_dictionaries = []
result_dictionaries = []
distinct_candidates = []
list_for_summary = []
winner = ''
max_votes = 0

# Read election_data.csv
with open(input_path, 'r') as input_file:
    reader = csv.reader(input_file)
    headers = next(reader)
    for ballot, county, candidate in reader:
        data_dictionary = {}
        data_dictionary['ballot']           = ballot
        data_dictionary['county']           = county
        data_dictionary['candidate']        = candidate
        original_dictionaries.append(data_dictionary)

# The total number of votes cast
total_votes = len(original_dictionaries)
distinct_candidates.append(original_dictionaries[0]['candidate'])

# A complete list of candidates who received votes
for dict in range(len(original_dictionaries)):
    if original_dictionaries[dict]['candidate'] not in distinct_candidates:
        distinct_candidates.append(original_dictionaries[dict]['candidate'])

for name in distinct_candidates:
    candidate_dictionary = {}
    candidate_dictionary['name']        = name 
    candidate_dictionary['votes']       = 0 
    result_dictionaries.append(candidate_dictionary)

# The percentage of votes each candidate won and 
# The total number of votes each candidate won
for index2 in range(len(result_dictionaries)):
    for index1 in range(len(original_dictionaries)):
        if original_dictionaries[index1]['candidate'] == result_dictionaries[index2]['name']:
            result_dictionaries[index2]['votes'] += 1 
    result_dictionaries[index2]['percent'] = 100 * result_dictionaries[index2]['votes'] / total_votes

# The winner of the election based on popular vote
winner = result_dictionaries[0]['name']
max_votes = result_dictionaries[0]['votes']
for index2 in range(len(result_dictionaries)):
    if result_dictionaries[index2]['votes'] > max_votes:
        max_votes = result_dictionaries[index2]['votes'] 
        winner = result_dictionaries[index2]['name'] 
    list_for_summary.append(f"{result_dictionaries[index2]['name']}: {result_dictionaries[index2]['percent']:.3f}% ({result_dictionaries[index2]['votes']})")

output_list = [
    [f"Election Results"],
    [f"-" * 25],
    [f"Total votes: {total_votes}"],
    ["-" * 25],
    [f"{list_for_summary}"],
    ["-" * 25],
    [f'Winner: {winner}'],
    ["-" * 25]
]

# Write results.txt and print to screen
with open(output_path, 'w', newline = '') as output_file:
    for line in output_list: 
        for i in range(len(line)):
            if line[i] == f"{list_for_summary}":
                for index2 in range(len(list_for_summary)):
                    print(list_for_summary[index2])
                    output_file.write(list_for_summary[index2])
                    output_file.write('\n')
            else: 
                print(line[i])
                output_file.write(line[i])
                output_file.write('\n')        