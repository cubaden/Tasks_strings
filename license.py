# Problem #4: License Key Formatting

# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.
 
# Example 1:
# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
# Example 2:
# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

#!/usr/bin/python3
import sys, string, re

if len(sys.argv) < 3:
	print("you passed in only ", len(sys.argv), "argument(s). 3 is needed")
	exit
print("those arguments are: ", str(sys.argv))

s = str(sys.argv[1]).upper()
k = int(sys.argv[2])

s = re.sub(r'-', '', s)

first_n = len(s) % k

s1 = s[:first_n]
s2 = s[first_n:]

result = [s2[y - k:y] for y in range(k, len(s2) + k, k)]
str_result = "-".join(result)

if (first_n > 0):
	print(s1 + '-' + str_result)
else:
	print(str_result)