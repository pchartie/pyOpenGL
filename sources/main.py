import sys
from gl_init                       import gl_init
from my_class.Cube                 import Cube
from my_class.KeyboardEvent        import KeyboardEvent
from my_class.MainGame             import MainGame

if __name__ == '__main__':
    gl_init()
    try:
        cube = Cube('../Cube')
    except:
        print('The cube file cannot be found or is corrupted')
        sys.exit()
    event = KeyboardEvent()
    game = MainGame(cube)
    while True:
        game.loop(cube, event)
