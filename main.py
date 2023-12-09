# Author: Dingan Li
# Date: 12/8/2023
# Description: game main function
import GameEngine

game=GameEngine.GameEngine #create game
game.constructor(game)
game.initializeGame(game)
game.intro(game)
while True: #loop unitl game end
    game.remainingVeggies(game)
    game.printField(game)
    game.moveRabbits(game)
    game.moveCaptain(game)
    game.moveSnake(game)
    if game.countVeggies(game)==0: #check number of veggie
        break
game.gameOver(game) #print result and save score
game.highScore(game)
# VeggieFile1.csv   VeggieFile2.csv

