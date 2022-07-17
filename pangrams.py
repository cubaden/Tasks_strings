# Problem #2: Pangrams
# The sentence "A quick brown fox jumps over the lazy dog" contains every single letter in the alphabet.
# Such sentences are called pangrams. You are to write a method getMissingLetters, which takes a String, sentence,
# and returns all the letters it is missing (which prevents it from being a pangram).
# You should ignore the case of the letters in sentence, and your return should be all upper case letters, in alphabetical order. 

#!/usr/bin/python3
import sys
import string

if len(sys.argv) < 2:
	print("you passed in only ", len(sys.argv), "argument(s). 3 is needed")
print("those arguments are: ", str(sys.argv))

s = str(sys.argv[1]).upper()

letters = list(string.ascii_uppercase)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for c in s:
	if c in letters:
		letters.remove(c)

if 0 == len(letters):
    print("yes")
else:
    print("no")
    print(str(letters))