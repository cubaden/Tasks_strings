# Problem #1: String Rotation
# Write a function which checks if one string is a rotation of other string.

# if s1 = "helloworld" then the following are some of its rotated versions:
# elloworldh
# lloworldhe
# loworldhel
# oworldhell
# worldhello

#!/usr/bin/python3
import sys

if len(sys.argv) < 3:
	print("you passed in only ", len(sys.argv), "argument(s). 3 is needed")
print("those arguments are: ", str(sys.argv))

#for arg in sys.argv:
#	print("Argument {0} {1}".format( i , str(arg) )
	
s = str(sys.argv[1])
test = str(sys.argv[2])

#test = input()
# find first character of s in input string
n = test.find(s[0])

# substring 1 from start of s to n
s1 = test[0:n]

# substring 2 from n to end of test
s2 = test[n:len(s)]

if s == s2 + s1:
    print("yes")
else:
    print("no")