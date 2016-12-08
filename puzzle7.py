import re

hypernet_regex = re.compile(r"\[([a-z]+)]")
seq_regex = re.compile(r"(^|])([a-z]+)($|\[)")


def is_abba(string):
    # get 4grams of sequence
    flag = False
    four_grams = list(zip(*[string[i:] for i in range(4)]))
    for item in four_grams:
        # check if reversed and not same letter
        if (item[0]+item[1] == (item[2]+item[3])[::-1]) and (item[0] != item[1]):
            flag = True
    return flag


def supports_tls(string):
    hypernets = hypernet_regex.findall(string)
    sequences = [x[1] for x in seq_regex.findall(string)]

    for hyp in hypernets:
        if is_abba(hyp):
            return False
    for seq in sequences:
        if is_abba(seq):
            return True

    return False

with open('puzzle_inputs/input7.txt') as f:
    strings = f.readlines()
    strings = [x.strip('\n') for x in strings]

tally = [supports_tls(x) for x in strings]
print(tally.count(True))
