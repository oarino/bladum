from sys import exit
from random import randint

from death import Death
from engine import Engine
from scene import Scene
from corridor import Corridor
from maze import Maze
from cementery import Cementery
from finished import Finished
from mapa import Map
from tomb import Tomb


a_map = Map('corridor')
a_game = Engine(a_map)
a_game.play()


