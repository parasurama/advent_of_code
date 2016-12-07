import pandas as pd
import csv

# read puzzle input and break codes into column
codes = []
with open('puzzle_inputs/input6.txt') as f:
    reader = csv.reader(f)
    for row in reader:
        codes.append([x for x in row[0]])
print(codes)

# convert code to dataframe
df = pd.DataFrame(codes)
print(df)

######################## PART 1 ################################
# get most frequently occcuring letter
message = []
# get max of each column
for i in df.columns:
    message.append(df[i].mode()[0])
print(message)

######################## PART 2 ################################
# get least freq. occuring letter by looking at value counts and choosing last element
part2_message = []
for i in df.columns:
    part2_message.append(df[i].value_counts().index[-1])
print(part2_message)
