import re

hypernet_regex = re.compile(r"\[([a-z]+)]")
seq_regex = re.compile(r"(^|])([a-z]+)($|\[)")


def is_abba(string):
    # get 4grams of sequence
    four_grams = zip(*[string[i:] for i in range(4)])
    for item in four_grams:
        # check if reversed and not same letter
        if (item[0]+item[1] == (item[2]+item[3])[::-1]) and (item[0] != item[1]):
            return True


def supports_tls(string):
    hypernets = hypernet_regex.findall(string)
    sequences = (x[1] for x in seq_regex.findall(string))

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

############################## PART 2 ###################################


def find_aba(string):
    # get 3grams of string
    tri_grams = list(zip(*[string[i:] for i in range(3)]))
    abas = []
    for item in tri_grams:
        if item[0] == item[2] != item[1]:
            abas.append(item)
    return abas


def supports_ssl(string):
    hypernets = hypernet_regex.findall(string)
    supernets = [x[1] for x in seq_regex.findall(string)]
    for sup in supernets:
        for hyp in hypernets:
            abas = find_aba(sup)
            hyp_trigrams = zip(*[hyp[i:] for i in range(3)])
            for item in abas:
                for ht in hyp_trigrams:
                    if item[0] == ht[1] and (item[1] == ht[0] == ht[2]):
                        return True


p2_tally = [supports_ssl(x) for x in strings]
print(p2_tally.count(True))


