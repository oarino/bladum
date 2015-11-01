from scene import Scene

class Finished(Scene):

    def enter(self):
        print "Great man!! You almost die."
        print "However you are alive and sane."
        return 'finished'
