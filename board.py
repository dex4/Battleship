from tkinter import *
import sys
sys.path.append('../')
from replace import *
import random
class GameBoard:
    def __init__(self):
        self._board = Tk()
        self._visited = []
        self.initPlayerGrid()
        self.initBotGrid()
        self.init_fields()
        self.initWindowLayout()
        self.botPlace()

    def initWindowLayout(self):
        playerTitle = Label(self._board, text="Player Board")
        playerTitle.grid(row=0, column=1)
        botTitle = Label(self._board, text="EnemyBoard")
        botTitle.grid(row=0, column=10)
        #Battleship input
        Radiobutton(self._board, text="Vertically", variable=self._ort, value=0).grid(row=10, column=0, sticky=W)
        Radiobutton(self._board, text="Horizontally", variable=self._ort, value=1).grid(row=11, column=0, sticky=W)
        self._typeLabel = Label(self._board, text="Ship type:")
        self._typeLabel.grid(row=12, column=0)
        Radiobutton(self._board, text="Battleship", fg="red", variable=self._shipType, value=1).grid(row=13, column=0, sticky=W)
        Radiobutton(self._board, text="Cruiser", fg="blue", variable=self._shipType, value=2).grid(row=14, column=0, sticky=W)
        Radiobutton(self._board, text="Destroyer", fg="green", variable=self._shipType, value=3).grid(row=15, column=0, sticky=W)

    def initPlayerGrid(self):
        self._playerGrid = []
        self._playerTargetGrid = []
        for i in range(8): #Rows
            self._playerGrid.append([])
            for j in range(8): #Columns
                b = Button(self._board, text="", width="2", bg="white", command=lambda row=i, column=j: self.placeTile(row, column))
                self._playerGrid[i].append(b)
                self._playerGrid[i][j].grid(row=i+1, column=j+2)

    def initBotGrid(self):
        self._botGrid = []
        self._botTargetGrid = []
        for i in range(8): #Rows
            self._botGrid.append([])
            for j in range(8): #Columns
                b = Button(self._board, text="", width="2", bg="white", fg="black", command=lambda row=i, column=j: self.shoot(row, column))
                self._botGrid[i].append(b)
                self._botGrid[i][j].grid(row=i+1, column=j+12)

    def init_fields(self):
        #Ship Variables
        self._shipType = IntVar()
        self._orientation = Label(self._board, text="Orientation:")
        self._orientation.grid(row=9, column=0)
        self._ort = IntVar()
        self._bTiles = 0
        self._cTiles = 0
        self._dTiles = 0
        self._playerTotal = 9
        self._botTotal = 9

    def shoot(self, r, c):
        if(self._botGrid[r][c]["fg"] != "black"):
            self._botGrid[r][c].configure(bg="red", text="X", state="disabled")
            self._botTotal -=1
            print("Bot left: ", self._botTotal)
            if(self._botTotal <= 0):
                self._endTimes = Tk()
                statusText = Label(self._endTimes, text="You WIN!\nCongratulations!")
                statusText.pack()
                status = Button(self._endTimes, text="Cool!", command=self._endTimes.destroy)
                status.pack()
        else:
            self._botGrid[r][c].configure(bg="gray", text="M", state="disabled")
        if(self._playerTotal > 0):
            self.botShoot()

    def botPlace(self):
        #placing Battleship
        self._botGrid = getIndex(4, self._botGrid, "red")
        self._botGrid = getIndex(3, self._botGrid, "blue")
        self._botGrid = getIndex(2, self._botGrid, "green")

    def botShoot(self):
        valid = False
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        while(valid == False):
            if([i, j] in self._visited):
                i = random.randint(0, 7)
                j = random.randint(0, 7)
                valid = False
            else:
                self._visited.append([i, j])
                valid = True
        if(self._playerGrid[i][j]["back"] != "white"):
            self._playerTotal -=1
            print("Player left:", self._playerTotal)
            if(self._playerTotal == 0):
                self._endTimes = Tk()
                statusText = Label(self._endTimes, text="You lose!\nA random placing bot just beat you..")
                statusText.pack()
                status = Button(self._endTimes, text="Oh.. okay!", command=self._endTimes.destroy)
                status.pack()
            self._playerGrid[i][j]["back"] = "white"
        self._playerGrid[i][j]["text"] = "X"
        self._playerGrid[i][j].configure(state="disabled")

    def placing(self, colour, nrTiles, sT, r, c, nr):
        tiles = nr
        if(tiles == 0):
            self._playerGrid[r][c].configure(bg=colour, state="disabled", fg="black")
            tiles = 1
        elif(tiles < nrTiles):
            if(self._ort.get() == 0):
                if(r==0):
                    if(self._playerGrid[r+1][c]["back"] == colour):
                        self._playerGrid[r][c].configure(bg=colour, state="disabled")
                        tiles += 1
                elif(r == 7):
                    if(self._playerGrid[r-1][c]["back"] == colour):
                        self._playerGrid[r][c].configure(bg=colour, state="disabled")
                        tiles += 1
                elif(r > 0 and r < 7):
                    if(self._playerGrid[r+1][c]["back"] == colour):
                        self._playerGrid[r][c].configure(bg=colour, state="disabled")
                        tiles += 1
                    if(self._playerGrid[r-1][c]["back"] == colour):
                        self._playerGrid[r][c].configure(bg=colour, state="disabled")
                        tiles += 1
            if(self._ort.get() ==1):
                if(c==0):
                    if(self._playerGrid[r][c+1]["back"] == colour):
                        self._playerGrid[r][c].configure(bg=colour, state="disabled")
                        tiles += 1
                elif(c == 7):
                    if(self._playerGrid[r][c-1]["back"] == colour):
                        self._playerGrid[r][c].configure(bg=colour, state="disabled")
                        tiles += 1
                elif(c > 0 and c < 7):
                    if(self._playerGrid[r][c+1]["back"] == colour):
                        self._playerGrid[r][c].configure(bg=colour, state="disabled")
                        tiles += 1
                    if(self._playerGrid[r][c-1]["back"] == colour):
                        self._playerGrid[r][c].configure(bg=colour, state="disabled")
                        tiles += 1
        elif(tiles == nrTiles):
            self._errorBoard = Tk()
            errorButton = Button(self._errorBoard, text="Okay!", command=self._errorBoard.destroy)
            errorButton.pack()
            errorLabel = Label(self._errorBoard, text= sT + "\nfully\nplaced.")
            errorLabel.pack()
        return tiles
        
    def placeTile(self, r, c):
        sT = self._shipType.get()
        if(sT == 0):
            self._errorBoard = Tk()
            errorButton = Button(self._errorBoard, text="Okay!", command=self._errorBoard.destroy)
            errorButton.pack()
            errorLabel = Label(self._errorBoard, text="You must select\nthe ship type.")
            errorLabel.pack()
        else:
            if(sT == 1):
                self._bTiles = self.placing("red", 4, "Battleship", r, c, self._bTiles)
            if(sT == 2):
                self._cTiles = self.placing("blue", 3, "Cruiser", r, c, self._cTiles)
            if(sT == 3):
                self._dTiles = self.placing("green", 2, "Destroyer", r, c, self._dTiles)

board = GameBoard()
mainloop()
