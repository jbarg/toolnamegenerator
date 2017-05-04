import random
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Tool name generator')
    parser.add_argument('-b', '--beginn', dest='beginn', required=False,
                                        help='set first character')
    return parser.parse_args()

args = parse_args()
first = open('adjectives.txt', 'r').readlines()
second = open('nouns.txt', 'r').readlines()


first_tmp = []
if args.beginn is not None:
    allowedChar = args.beginn[0]
    for word in first:
        if word[0] is allowedChar:
            first_tmp.append(word)

    first = first_tmp

name = first[random.randint(0,len(first))].strip()
name += second[random.randint(0,len(second))].strip()

name.strip()
print name.upper()
