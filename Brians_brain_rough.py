
"""
This is conway's and we will modify it for brian's brain 
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

ON = 1
OFF = 0
DYING = -1
states = [ON, OFF, DYING]


"""

This is an older grid I've put on ice, but kept in case I mess up the animation and need to debug, because I know this works
def updateGrid(grid, N): 

	#Here we will updoot our grid. After that, back in the while loop, print a new grid

	#we need to copy the grid, we will place the FUTURE value after this update in future grid
	futureGrid = grid.copy()

	
	for y in range(N):
		for x in range(N):

			#add together a cell's 8 homies
			# we'll ur 'toriodal bounder conditions, ei, we'll basically have any values that 
			# go over 'wrap around' so to speak 
			nearSum = int(grid[(x-1)%N, (y-1)%N] + grid[x, (y-1)%N] + grid[(x+1)%N, (y-1)%N] +
				grid[(x-1)%N, y] + grid[(x+1)%N, y] +
			   grid[(x-1)%N, (y+1)%N] + grid[x, (y+1)%N] + grid[(x+1)%N, (y+1)%N])

			#deBuggin 

			#Just a template, please deyeet me
			#if ( == -1):
			#	nearSum = nearSum + 1

			

			#Time to make a disgusting mess
			#forgive me python gods for I know there must be a better way
			if (int(grid[(x-1)%N, (y-1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[x, (y-1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[(x+1)%N, (y-1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[(x-1)%N, y]) == -1):
				nearSum = nearSum + 1


			if (int(grid[(x+1)%N, y]) == -1):
				nearSum = nearSum + 1

			if (int(grid[(x-1)%N, (y+1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[x, (y+1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[(x+1)%N, (y+1)%N]) == -1):
				nearSum = nearSum + 1

			
			#print((grid[(x-1)%N, (y-1)%N] + grid[x, (y-1)%N] + grid[(x+1)%N, (y-1)%N] +
			#	grid[(x-1)%N, y] + grid[(x+1)%N, y] +
			#   grid[(x-1)%N, (y+1)%N] + grid[x, (y+1)%N] + grid[(x+1)%N, (y+1)%N]))
			

			#print(nearSum)

			
			#print( ((x-1)%N, (y-1)%N), (x, (y-1)%N), ((x+1)%N, (y-1)%N),
			#	((x-1)%N, y) ,((x+1)%N, y) , 
			#	((x-1)%N, (y+1)%N) , (x, (y+1)%N) , ((x+1)%N, (y+1)%N))
			#print(nearSum)
			

			#Brian's brain thyme, rules change here
			if grid[x, y] == ON:
				#If it's on, it gets set to start dying, big L 				
				futureGrid[x, y] = DYING
			elif grid[x, y] == DYING:
				futureGrid[x, y] = OFF
			else:
				#Reproduction
				if nearSum == 2:
					futureGrid[x, y] = ON
			

			
	grid[:] = futureGrid[:]

"""

# "Jose, why did you put the nextFrame variable first, if before grid and N were first. ? Wouldn't think break things?" 
# YES. MATPLOT LIB DOESNT LIKE IT THERE THO
def updateGrid(apperentlyFourVariablesAreBeingSentIDontBeliveItButThisFixesIt, nextFrame, grid, N): 

	#Here we will updoot our grid. After that, back in the while loop, print a new grid

	#we need to copy the grid, we will place the FUTURE value after this update in future grid
	futureGrid = grid.copy()

	
	for y in range(N):
		for x in range(N):

			#add together a cell's 8 homies
			# we'll ur 'toriodal bounder conditions, ei, we'll basically have any values that 
			# go over 'wrap around' so to speak 
			nearSum = int(grid[(x-1)%N, (y-1)%N] + grid[x, (y-1)%N] + grid[(x+1)%N, (y-1)%N] +
				grid[(x-1)%N, y] + grid[(x+1)%N, y] +
			   grid[(x-1)%N, (y+1)%N] + grid[x, (y+1)%N] + grid[(x+1)%N, (y+1)%N])

			#deBuggin 

			""" Just a template, please deyeet me
			if ( == -1):
				nearSum = nearSum + 1

			"""

			#Time to make a disgusting mess
			#forgive me python gods for I know there must be a better way
			if (int(grid[(x-1)%N, (y-1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[x, (y-1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[(x+1)%N, (y-1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[(x-1)%N, y]) == -1):
				nearSum = nearSum + 1


			if (int(grid[(x+1)%N, y]) == -1):
				nearSum = nearSum + 1

			if (int(grid[(x-1)%N, (y+1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[x, (y+1)%N]) == -1):
				nearSum = nearSum + 1

			if (int(grid[(x+1)%N, (y+1)%N]) == -1):
				nearSum = nearSum + 1

			"""
			print((grid[(x-1)%N, (y-1)%N] + grid[x, (y-1)%N] + grid[(x+1)%N, (y-1)%N] +
				grid[(x-1)%N, y] + grid[(x+1)%N, y] +
			   grid[(x-1)%N, (y+1)%N] + grid[x, (y+1)%N] + grid[(x+1)%N, (y+1)%N]))
			"""

			#print(nearSum)

			"""
			print( ((x-1)%N, (y-1)%N), (x, (y-1)%N), ((x+1)%N, (y-1)%N),
				((x-1)%N, y) ,((x+1)%N, y) , 
				((x-1)%N, (y+1)%N) , (x, (y+1)%N) , ((x+1)%N, (y+1)%N))
			print(nearSum)
			"""

			#Brian's brain thyme, rules change here
			if grid[x, y] == ON:
				#If it's on, it gets set to start dying, big L 				
				futureGrid[x, y] = DYING
			elif grid[x, y] == DYING:
				futureGrid[x, y] = OFF
			else:
				#Reproduction
				if nearSum == 2:
					futureGrid[x, y] = ON
			

	#update the next frame, now that it's been worked on
	nextFrame.set_data(futureGrid)
	grid[:] = futureGrid[:]

	return nextFrame

def main():
	#set our grid size 
	N = 100

	#create Grid
	grid = np.array([])

	#For now lets just toss in random numbers, nice format stuff later, also brian's brain ]
	#gets extra value here 
	grid = np.random.choice(states, N*N, p=[0.5, 0.3, 0.2]).reshape(N,N)

	i=0

	#sanity check 
	print(grid)
	print("first grid")

	""" abomination for how I was displaying this at first
	while i < 1000:
		i += 1
		updateGrid(grid, N)
		print(grid)




	#our actual output
	print(grid)
	""" 

	# More humane attempt at animation. My apologies if a bit rough
	# will be using plt lib from matplotlib to keep track of state
	# will be using animation from matplotlib...for animation

	#set up, create  and axes subplot for animation
	gridFig, axES = plt.subplots()

	#set up 
	nextFrame = axES.imshow(grid)

	#a lil libray useage I don't completely understand in order to make things print pretty
	brainsAnimation = animation.FuncAnimation(gridFig, updateGrid, fargs=(nextFrame, grid, N ) ) 

	#actually showing the animation
	plt.show()


if __name__ == '__main__':
		main()
