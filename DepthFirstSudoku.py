# abstracting iterating functions
# 	rowCols, boxNeighbors

import sudokuText

class Board(object):
	def __init__(self):
		self.squares = {}
		self.empties = []
		self.buildSquares()

### Initializing functions
	def buildSquares(self):
		for x in range(1, 10):
			for y in range(1, 10):
				self.squares[(x,y)] = Square(x, y, None)

	def pre_fill(self, values):  # values = [[x, y, val], [x, y, val], ...]
		for data in values:
			self.markSquare(data[0], data[1], data[2])

	def markSquare(self, x, y, val):
		self.squares[(x,y)].fill(val)
		for i in range(1, 10):
			self.squares[(x,i)].cannotBe(val)   # iterates over row
			self.squares[(i,y)].cannotBe(val)   # iterates over column
		for square in self.iterBox(x, y):
				square.cannotBe(val)			# iterates over box

## Sort squares for DFS efficiency
	def sort_squares(self):
		byLength = { 0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [] }
		for square in self.squares.itervalues():
			byLength[len(square.couldBe)].append(square)
		for i in range(1, 10):
			self.empties.extend(byLength[i])

### Depth-first search operations
	def depth_first(self, depth=0):
		if depth == len(self.empties):
			print 'Puzzle solved!'
			print self.pretty()
			assert False					# cancel operation
		square = self.empties[depth]
		for value in square.couldBe:		# test possible values
			if not self.legal_move(square.x, square.y, value):
				continue					# pass over illegal moves
			square.val = value
			self.depth_first(depth+1)
			square.val = None				# resets value if dead end reached
		return

	def legal_move(self, x, y, value):
	# check other squares in the same row, column and box for duplicate value
		for i in range(1, 10): 
			if self.squares[(x,i)].val == value:
				return False
			if self.squares[(i,y)].val == value:
				return False
		for square in self.iterBox(x, y):
			if square.val == value:
				return False
		return True

### Helper functions
	def pretty(self):
		output = '\n'
		for y in range(1, 10):
			row = ''
			for x in range(1, 10):
				val = self.squares[(x,y)].val
				row += str(val)
				if x == 3 or x == 6:
					row += '|'
				else:
					row += ' '
			output += row + '\n'
			if y == 3 or y == 6:
				output += '-----------------\n'
		return output

	def iterBox(self, x, y):  # iterates over all squares in the same 3x3 box
		for a in boxRange(x):
			for b in boxRange(y):
				yield self.squares[(a,b)]

def boxRange(x):
	if   1 <= x <= 3:
		return range(1, 4)   # or [1,2,3]
	elif 4 <= x <= 6:
		return range(4, 7)
	else:
		return range(7, 10)

class Square(object):
	def __init__(self, x, y, val):
		self.x   = x
		self.y   = y
		self.val = val
		self.couldBe = [1,2,3,4,5,6,7,8,9]

	def fill(self, val):
		self.val     = val
		self.couldBe = []

	def cannotBe(self, val):
		try:
			self.couldBe.remove(val)
		except:			# "remove" throws an error if the value is not found
			return

# Run full operation
def DFS_Sudoku(doc):
	board = Board()
	board.pre_fill(sudokuText.parser(doc))
	board.sort_squares()
	board.depth_first()

nemesis = 'nemesis.txt'
DFS_Sudoku(nemesis)
