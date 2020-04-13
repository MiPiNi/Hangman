import random


def random_word(min_lenght:int):
    if min_lenght > 0:
        with open("WORDLIST.txt") as f:
            num_lines = file_len("WORDLIST.txt")
            lines = f.readlines()
            i = 0
            while True:
                random_line_number = random.randrange(0, num_lines, 1)
                if len(lines[random_line_number])-1 >= min_lenght:
                    return lines[random_line_number]
                else:
                    i += 1
                    if i <= num_lines:
                        continue
                    else:
                        return -1
    else:
        return -2


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1




