import pandas as pd
import re
from collections import Counter

df = pd.read_csv('puzzle_inputs/input4.txt', header=None)
df = df.rename(columns={0: 'name'})

#regexes
letters_regex = re.compile(r".+?(?=\d)")
checksum_regex = re.compile(r"\[([a-z]{5})\]")
id_regex = re.compile(r"\d{3}")

# get letters, checksum only
df['letters'] = df['name'].apply(lambda x: letters_regex.search(x).group(0).replace('-', ''))
df['check_sum'] = df['name'].apply(lambda x: checksum_regex.search(x).group(1))
df['ids'] = df['name'].apply(lambda x: int(id_regex.search(x).group(0)))

# most common letters
def most_common_letters(string):
    c = Counter(string)
    # get counts of elements
    count_tuples = c.most_common(30)
    # sort by count (reverse) and then by alphabetical order
    sorted_tuples = sorted(count_tuples, key=lambda x: (-x[1], x[0]))[:5]
    letters = ''.join([x[0] for x in sorted_tuples])
    return letters
df['common_letters'] = df['letters'].map(most_common_letters)

# real rooms
df_real_rooms = df[df['common_letters'] == df['check_sum']]

# sum of ids of real rooms
answer = df_real_rooms['ids'].sum()
print(answer)