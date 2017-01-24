from direct.showbase import DirectObject
from panda3d.core import *

class Listener(DirectObject.DirectObject):
    def __init__(self, app):
        self.app = app
        self.accept('space', self.rodney_shoots)
        self.accept('r', self.rodney_reloads)
        self.accept('b', self.rodney_block)
        self.accept('b-up', self.rodney_unblock)

    def rodney_shoots(self):
        ##### THIS IS PURELY FOR TESTING PURPOSES
        prof = self.app.Profs[self.app.prof_count-1]
        self.app.rodney.shoot(prof.getPos())
    def rodney_reloads(self):
        self.app.rodney.charge()
    def rodney_block(self):
        self.app.rodney.blocks()
    def rodney_unblock(self):
        self.app.rodney.unblocks()
    def printlocation(self):
        print self.app.cam.getPos()
        print self.app.cam.getHpr()
        print self.app.cam.getScale()