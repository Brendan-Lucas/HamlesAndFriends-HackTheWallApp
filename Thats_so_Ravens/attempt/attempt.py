#panda load attempt.
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpPosInterval
from panda3d.core import *

class AttemptLoad(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        #add Ambient Light
        ambientLight = AmbientLight("AmbLight")
        ambientLight.setColor(Vec4(1, 1, 1, 1))
        ambientLightNodePath = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNodePath)
        #set Background colour.
        #self.setBackgroundColor(0, 0, 0)
        #load Ring Model
        self.ring = self.loader.loadModel('models/ring')
        self.ring.reparentTo(self.render)
        self.ring.setPos(0,0,0)

        self.cam.setPos(0, -32, 10)


        self.arod = self.loader.loadModel('models/A_Rod_Mod')
        self.arod.setScale(0.001, 0.001, 0.001)
        self.arod.reparentTo(self.ring)
        self.arod.setPos(0, 0, 4.5)


attempt = AttemptLoad()
attempt.run()
