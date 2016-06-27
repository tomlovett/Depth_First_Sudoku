game = 'game.txt'

def load_game(doc):
    endList = []
    inFile = open(doc, 'r', 0)
    for line in inFile:
        endList.append(line.strip())
    return endList

##load_game('game.txt')

def parser(doc):
    text = load_game(doc)
    row = 1
    values = []
    for y in range(1,10):
        line = text[y-1]
        for x in range(1,10):
            if line[x-1].isdigit() is True:
                values.append([x,y,int(line[x-1])])
    return values
