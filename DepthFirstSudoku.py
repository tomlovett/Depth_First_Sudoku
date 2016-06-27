import sudokuText

class Board(object):
	def __init__(self):
		self.squares  = {}
		self.sorted   = []  # open squares, sorted by number of possible values
		self.buildSquares()

	def buildSquares(self):
		for x in range(1, 10):
			for y in range(1, 10):
				self.squares[(x,y)] = Square(x, y, None)

	def pre_fill(self, values):  # values = [[x, y, val], ...]
		for data in values:
			self.markSquare(data[0], data[1], data[2])

	def markSquare(self, x, y, val):
		self.squares[(x,y)].fill(val)
		for i in range(1, 10):
			self.squares[(x,i)].cannotBe(val)   # clear row
			self.squares[(i,y)].cannotBe(val)   # clear column
		for a in boxRange(x):
			for b in boxRange(y):
				self.squares[(a,b)].cannotBe(val)

	def legal_move(self, square, value):
		x = square.x
		y = square.y
		for i in range(1, 10):
			if self.squares[(x,i)].val == value:
				return False
			if self.squares[(i,y)].val == value:
				return False
		for a in boxRange(x):
			for b in boxRange(y):
				if self.squares[(a,b)].val == value:
					return False
		return True

	def depth_first(self, depth=0):
		if depth = len(self.sorted):
			print 'Puzzle solved!'
			assert False					# cancel operation
		square = self.sorted[depth]
		for value in square.couldBe:		# test possible values
			if not self.legal_move(square, value):
				continue					# pass over illegal moves
			square.val = value
			self.depth_first(depth+1)		# run one level deeper
			square.val = None				# resets value if dead end reached
		return

	def sort_squares(self):
	# This function assembles the open squares in the most efficient order 
	#	for depth-first search  (see footnote: "Sorting by efficiency")
	# Squares with fewer possible values are put at the front
		for i in range(1, 10):
			for square in self.squares.itervalues():
				if len(square.couldBe) == i:
					self.sorted.append(square)

def boxRange(x):		# see footnote: "boxRange"
	if   1 <= x <= 3:
		return range(1, 4)
	elif 4 <= x <= 6:
		return range(4, 7)
	else
		return range(7, 10)

class Square(object):
	def __init__(self, x, y, val):
		self.x = x
		self.y = y
		self.val = val
		self.couldBe = [1,2,3,4,5,6,7,8,9]

	def fill(self, val):
		self.val     = val
		self.couldBe = []

	def cannotBe(self, val):
		try:
			self.couldBe.remove(val)
		except:
			return

# Run full operation
def DFS_Sudoku(text):
	board = Board()
	print 'board created'
	board.pre_fill(sudokuText.parser(text))
	print 'board pre-filled: ', board
	board.sort_squares()
	print 'board.sorted: ', board.sorted
	board.depth_first(0)

nemesis = 'nemesis.txt'
DFS_Sudoku(nemesis)

"""
Footnotes:

Sorting for efficiency
	In this depth-first search it is most efficient to test values

boxRange

"""


