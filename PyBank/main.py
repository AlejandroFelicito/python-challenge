import csv
import os

input_path = os.path.join('.', 'Resources', 'budget_data.csv')
output_path = os.path.join('.', 'analysis', 'results.csv')
month_count = 0
net_total_amount = 0
dictionaries = []
goa_increase = 0
goa_decrease = 0

# Read budget_data.csv
# The net total amount of "Profit/Losses" over the entire period
with open(input_path, 'r') as input_file:
    reader = csv.reader(input_file)
    headers = next(reader)
    for row in reader:
        net_total_amount += int(row[1])
        data_dictionary = {}
        data_dictionary['date']             = row[0]
        data_dictionary['profit_losses']    = row[1]
        dictionaries.append(data_dictionary)

# The changes in "Profit/Losses" over the entire period 
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
dictionaries[0]['delta'] = '0'
goa_increase = dictionaries[0]
goa_decrease = dictionaries[0]
for dict in range(1, len(dictionaries)):
    dictionaries[dict]['delta'] = int(dictionaries[dict]['profit_losses']) - int(dictionaries[dict - 1]['profit_losses'])
    if int(dictionaries[dict]['delta']) > int(goa_increase['delta']):
        goa_increase = dictionaries[dict]
    if int(dictionaries[dict]['delta']) < int(goa_decrease['delta']):
        goa_decrease = dictionaries[dict]
    
# The total number of months included in the datase
# The average of the changes in "Profit/Losses" over the entire period 
month_count = len(dictionaries)
max_index = len(dictionaries) - 1
avg_delta = (1 / max_index) * (int(dictionaries[max_index]['profit_losses']) - int(dictionaries[0]['profit_losses']))

output_list = [
    [f"Financial Analysis"],
    [f"------------------------------"],
    [f"Total Months: {month_count}"],
    [f"Total: ${net_total_amount}"],
    [f"Average Change: ${avg_delta:.2f}"],
    [f"Greatest Increase in Profits: {goa_increase['date']} (${goa_increase['delta']})"],
    [f"Greatest Decrease in Profits: {goa_decrease['date']} (${goa_decrease['delta']})"]
]

# Write results.csv 
with open(output_path, 'w', newline = '') as output_file:
    writer = csv.writer(output_file, delimiter = '\t')
    writer.writerows(output_list)

# Print to screen
for line in output_list: 
    for i in range(len(line)):
        print(line[i])