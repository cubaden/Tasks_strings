# A collection of particles is contained in a linear chamber. They all have the same speed, but some are headed toward the right and others are headed toward the left.
# These particles can pass through each other without disturbing the  motion of the particles,
# so all the particles will leave the chamber relatively quickly.
# We will be given the initial conditions by a String init containing at each position an 'L' for a leftward moving particle,
# an 'R' for a rightward moving particle, or a '.' for an empty location. init shows all the positions in the chamber.
# Initially, no location in the chamber contains two particles passing through each other. 

#W e would like an animation of the process. At each unit of time, we want a string showing occupied locations with an 'X' and unoccupied locations with a '.'. 

# Implement “animate” function which takes int - speed and std::string (or vector) containing initial condition. The speed is the number of positions each particle moves in one time unit. 

# The method will return a std::vector of std::string in which each successive element shows the 
# occupied locations at the next time unit. The first element of the return should show the occupied locations at the initial instant (at time = 0) in the 'X','.' format.
# The last element in the return should show the empty chamber at the first time that it becomes empty. 

# Constraints 
# - speed will be between 1 and 10 inclusive 
# - init will contain between 1 and 50 characters inclusive 
# - each character in init will be '.' or 'L' or 'R' 

#!/usr/bin/python3
import sys
import string

if len(sys.argv) < 2:
	print("you passed in only ", len(sys.argv), "argument(s). 3 is needed")
print("those arguments are: ", str(sys.argv))

input_str = str(sys.argv[1])
input_speed = int(sys.argv[2])

n = len(input_str)
x = range(n)
result_str = ""

for i in x:
	c = input_str[i]
	if c == 'R':
		print("new pos i's R = " + str(i + input_speed))
	elif c == 'L':
		print("new pos i's L = " + str(i - input_speed))
	else:
		print("same")
	
# Example 1:
# "..R....", 2 
# Returns: 
# { “..X....",
#   “....X..",
#   “......X",
#   "......." }
# The single particle starts at the 3rd position, moves to the 5th, then 7th, and then out of the chamber.
# Example 2:
# "RR..LRL", 3 