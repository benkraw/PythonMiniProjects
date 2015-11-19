from random import randint

def make_board(width, height): #Makes the board
    return [['X' for count in range(width)] for rows in range(height)]

def print_board(board): #Prints the board
    for row in board:
        print(' '.join(row))
    print('')

def nextFrame(myboard, height, width): #Displays next generation of cells

	temp = [["X" for x in xrange(width)] for x in xrange(height)] 
	numSurrounding = 0
	for i in range(height):
		for j in range(width):
			#Check around each cell
			if ( (i+1) < height and myboard[i + 1][j] == "." ):
				numSurrounding+=1
			if ( (i-1) >= 0 and myboard[i - 1][j] == "." ):
				numSurrounding+=1
			if ( (j+1) < width and myboard[i][j+1] == "." ):
				numSurrounding+=1
			if ( (j-1) >= 0 and myboard[i][j-1] == "." ):
				numSurrounding+=1
			if ( (i+1) < height and (j+1) < width and myboard[i+1][j+1] == "." ):
				numSurrounding+=1
			if ( (i+1) < height and (j-1) >= 0 and myboard[i+1][j-1] == "." ):
				numSurrounding+=1
			if ( (i-1) >= 0 and (j+1) < width and myboard[i-1][j+1] == "." ):
				numSurrounding+=1
			if ( (i-1) >= 0 and (j-1) >= 0 and myboard[i-1][j-1] == "." ):
				numSurrounding+=1
			#Apply the Rules 	
			if (numSurrounding <= 1 or numSurrounding > 4):
				temp[i][j] = "X" 
			elif(numSurrounding == 3):
				temp[i][j] = "."
			elif(numSurrounding == 2 or numSurrounding == 3):
				temp[i][j] = myboard[i][j]
			numSurrounding = 0;
			j += 1
		i += 1
	for i in range(height):
		for j in range(width):
			myboard[i][j] = temp[i][j]
			j+=1
		i+=1
	return myboard

def main():
	print "This is a program created on Conway's Game of Life"
	height = int(raw_input("Enter number of rows: "))
	width = int(raw_input("Enter number of columns: "))
	myboard = make_board(width, height)

	#Generate a 1/4 of the area for first generation of alive cells
	n = width * height
	sample_cell = n*.25
	i = 0
	while(i<sample_cell):
		x = randint(0, height-1)
		y = randint(0, width-1)
		myboard[x][y] = str(".")
		i +=1

	next = True
	first = True
	i = 0
	print_board(myboard)
	while(next):
		print "Generation " + str(i)
		i +=1
		check = raw_input("Enter y for next cycle, anything else to quit...")
		if check != "y":
			next = False
		else:
			if first:
				next_generation = nextFrame(myboard, height, width)
				print_board(next_generation)
				first = False
			else:
				next_generation = nextFrame(next_generation, height, width)
				print_board(next_generation)
	print "Exiting..."

main()
