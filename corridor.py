from scene import Scene

class Corridor(Scene):

    def enter(self):
        print "Until two weeks ago you were a calm farmer of Maine. You spent your whole time with your wife and your kids..."
        print "taking care of your farm."
        print "However womething happened two days ago. There was an eclipse for serveral hours and all your animals became crazy."
        print "Suddenly you heard your wife screaming and glasses being destroyed."
        print "You did not see anythin ... Just your wife scraming and someone (or something) who was carrying her."
        print "You have to react quickly ... So you took your axe and follow your wife's shouts. \n"
        print "After a while running you arrive to a cave near the Bladum's hill."
        print "Whitout doubt you go into the cave.\n"
        print "Once you are there ... What do you want to do?"
        print """
                1 - You run directly inside the cave following the figure. Type run
                2 - You take a deep breath, grab firmly the axe on your hands and proceed to explore the cave. Type walk
                3 - You are too afraid and leave your wife on her own destiny. Type leave
        
              """
        
        action = raw_input("> ")
        
        
        if action == 'run':
            print"You are an action man but also a stupid one."
            print"You did not think before going into the cave."
            print"Due to this you did not see the trap in front of you and it took you totally."
            print"You fall into a great hole in the middle of the corridor and, when you are on the ground,you get your neck brocken."
            return 'death'
        elif action == 'walk':
            print "Once you are inside you are able to see the great whole and avoid it."
            print "There is only one possibility to follow and is the door of a giant maze just in front of you."
            return 'maze'
        elif action == 'leave':
            print"You coward ... You leave alone your wife in the hands of the creature and return calmly to your own house."
            print"But destiny has bad humor"
            print"When you are coming back five horrendous creatures attack you."
            print"You are dead as well as your wife"
            return 'death'
        else:
            print "DOES NOT COMPUTE!"
            return 'corridor'
