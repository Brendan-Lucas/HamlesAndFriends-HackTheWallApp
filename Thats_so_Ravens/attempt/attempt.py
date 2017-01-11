#panda load attempt.
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpPosInterval
from panda3d.core import *

class AttemptLoad(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        ambientLight = AmbientLight("AmbLight")
        ambientLight.setColor(Vec4(1, 1, 1, 1))
        ambientLightNodePath = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNodePath)
        self.setBackgroundColor(0, 0, 0)
        self.ring = self.loader.loadModel('models/ring')
        self.ring.reparentTo(self.render)

attempt = AttemptLoad()
attempt.run()
