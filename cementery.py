from scene import Scene

class Cementery(Scene):

    def enter(self):
        
        print " You run inside of a horrible cementery."
        print " The hard smell of the death almost makes you movit"
        print " But then you hear again your wife's voice in the sorroundings and your courage resuscitates on you"
        print " Ok man is now or never ... Which path do you follow right or left?"
        
        action = raw_input("> ")
        
        if action == 'right':
            print " You had prefer not to have to see what you are seeing ... but this seems to be useless."
            print " You come back turn back your steps"
            return 'cementery'
        elif action == 'left':
            print " Steps sound louder each step you go into the cementery ..."
            return 'tomb'
        else:
            print "DOES NOT COMPUTE!"
            return 'cementery'    
