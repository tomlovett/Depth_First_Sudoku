# import

# fill in squares
# assemble cannotBe's
# sort squares: least -> most

# DFS

import sudokuText

def load_vals(text):
	return sudokuText.parser(text) 		# redundant?

def fill_board(values):		# values = [[x, y, val], ...]
	pass

class Board(object):
	def __init__(self):
		self.squares  = {}
		self.sorted   = []
		self.buildSquares()

	def buildSquares(self):
		for x in range(1, 10):
			for y in range(1, 10):
				self.squares[(x,y)] = Square(x, y, None)

	def markSquare(self, x, y, val):
		self.squares[(x,y)].fill(val)
		for i in range(1, 10):
			self.squares[(x,i)].cannotBe(val)   # clear row
			self.squares[(i,y)].cannotBe(val)   # clear column
		for a in boxRange(x):
			for b in boxRange(y):
				self.squares[(a,b)].cannotBe(val)

def boxRange(x):
	if   1 <= x <= 3:
		return range(1, 4)
	elif 4 <= x <= 6:
		return range(4, 7)
	else
		return range(7, 10)

class Square(object):
	def __init__(self, x, y, val):
		self.x   = x
		self.y   = y
		self.val = val
		self.couldBe = [1,2,3,4,5,6,7,8,9]

	def __lt__(self, other):   # one of these is redundant, I believe __gt__
		if len(self.couldBe) < len(other.couldBe):
			return True
		else
			return False

	def __gt__(self, other):
		if len(self.couldBe) > len(other.couldBe):
			return True
		else
			return False

	def fill(self, val):
		self.val     = val
		self.couldBe = []

	def cannotBe(self, val):
		try:
			self.couldBe.remove(val)
		except:
			return

	def valid(self, val):
		return val in self.couldBe

def depthFirstSudoku(board, depth=0):
	if depth == len(board.sorted):
		print 'Puzzle solved!'
		assert False
	square = board.sorted[depth]
	for value in square.couldBe:
		