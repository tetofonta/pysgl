from pysgl.game_manager import GameManager
from GameTestState import DemoState

game = GameManager()
game.init("FONTS")
game.addGameState(DemoState)
game.currentGameState = "DemoState"
game.run()
