from game import Game

game = Game('abc')

while not game.win:
    game.inputLetter()

