import random
from scene import Scene

class Tomb(Scene):

    def enter(self):

        monster_life_level = 13
        player_life_level = 10

    
        while player_life_level > 0:
            print " Choose updown or leftright hit with your axe"
            action = raw_input("> ")
            if action == 'updown':
                monster_life_level = monster_life_level - random.randint(0,3)
            elif action == 'leftright':
                monster_life_level = monster_life_level - random.randint(0,2)
            else:
                print "You failed, try again."

            print "The monster attacks you now"
            player_life_level = player_life_level - random.randint(0,2)

            print "You now have %r points of live" % player_life_level
            print "The monster now has %r points of live" % monster_life_level

            if player_life_level < 1 :
                print "Sorry man ... The monster is going to eat you an your wife"
                return 'death'
            elif monster_life_level < 1:
                print "The monster lies dead on your feet"
                print "You take your wife and runout as fast as possible"
                print "Great man ... you are a hero."
                return 'finished' 
            else:
                print "Combat continues"

       
