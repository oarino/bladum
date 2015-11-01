from scene import Scene

class Maze(Scene):

    def enter(self):
        
        print " Once in front of the maze's entrance you can follow the paths:"
        print " Right, center and left "
        print " Certainly your wife's voice comes from inside the maze..."
        print " But you could not say from where exactly."
        print " So ... make a guess and follow your instinct."
        print """
                Please type: right, center or left to make a choice
              """
    
        action = raw_input("> ")
    
        if action == 'right':
            print " You walk for about ten minutes but, clearly, you understand that this branch goes nothing."
            print " You come back to the entrance and take another choice."
            return 'maze'
        elif  action == 'center':
            print " Apparently everything was ok following this path."
            print " However in the last minute you see a bunch of small and ugly creatures which are staring fiercely at you."
            print " Finally one of them runs directly to you ... and the rest do the same after that."
            print " You fight with your axe but there are too many of them and you die in a circle of sorrow."
            return 'death'
        elif action == 'left':
            print "After of five minutes of walking you the maze is ended and you arrive to a new place ..."
            return 'cementery'
        else:
            print "DOES NOT COMPUTE!"
            return 'maze'
        
