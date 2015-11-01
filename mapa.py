from sys import exit
from random import randint

from death import Death
from scene import Scene
from corridor import Corridor
from maze import Maze
from cementery import Cementery
from finished import Finished
from tomb import Tomb



class Map(object):
    
    scenes = {
        'cementery' : Cementery(),
        'corridor' : Corridor(),
        'death' : Death(),
        'maze' : Maze(),
        'tomb' : Tomb(),
        'finished' : Finished(),
     }
    
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
