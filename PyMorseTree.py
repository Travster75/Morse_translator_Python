#Travis Bender

#Create the Node class
class NODE:
    #Default constructor
    def __init__(self):
        self.letter = ''
        self.left = None
        self.right = None

#Class for translations
class MorseTree:
    #Default constructor
    def __init__(self):
        self.root = NODE()
        self.createTree()

    #Creates the morse tree
    def createTree(self):
        #Opens the file to read
        f = open('morse.txt', 'r')

        #Gathers the data
        for line in f:
            morseLetter = line[0]
            morseSymbols = line[2:]
            morseSymbols = morseSymbols.strip()
            #Inserts into the tree
            self.insertNode(self.root, morseLetter, morseSymbols)

        #Close the file
        f.close()


    #Function to insert into the tree
    def insertNode(self, temp, morseLetter, symbols):
        #If reached end of morse code
        if len(symbols) == 0:
            temp.letter = morseLetter
        #If dot, go left
        elif symbols[0] == '.':
            if temp.left == None:
                temp.left = NODE()
                
            self.insertNode(temp.left, morseLetter, symbols[1:])
        #If dash, go right
        elif symbols[0] == '-':
            if temp.right == None:
                temp.right = NODE()

            self.insertNode(temp.right, morseLetter, symbols[1:])

    #Function to handle the recursive translate function
    def interpretMorse(self, morseSymbols):
        return self.translate(self.root, morseSymbols, '')

    #Translates the symbols to ASCII
    def translate(self, temp, morseSymbols, result):
        #If reached end of morse
        if len(morseSymbols) == 0:
            if temp != None:
                result += temp.letter;

            return result;
        #If dot, go left
        elif morseSymbols[0] == '.':
            return self.translate(temp.left, morseSymbols[1:], result)
        #If dash, go right
        elif morseSymbols[0] == '-':
            return self.translate(temp.right, morseSymbols[1:], result)
        #X represents end of morse sequence
        elif morseSymbols[0] == 'X':
            if temp != None:
                result += temp.letter

            #Two X's represnts a space
            if len(morseSymbols) > 1 and morseSymbols [1] == 'X':
                result += ' '

            #Begin at top
            return self.translate(self.root, morseSymbols[1:], result)
        #For unknown character
        else:
            if temp != None:
                result += temp.letter

            result += '?'
            #Begin at top
            return self.translate(self.root, morseSymbols[1:], result)
        
        
#Create the object
mTree = MorseTree()

morse = '....X.X.-..X.-..X---XX.--X---X.-.X.-..X-..X'

#Print the translated string
print(mTree.interpretMorse(morse))

