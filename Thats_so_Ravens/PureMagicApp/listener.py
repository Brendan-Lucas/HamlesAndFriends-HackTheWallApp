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
        self.app.rodney.shoot((-8, 8, 4.5))
    def rodney_reloads(self):
        self.app.rodney.charge()
    def rodney_block(self):
        self.app.rodney.blocks()
    def rodney_unblock(self):
        self.app.rodney.unblocks()