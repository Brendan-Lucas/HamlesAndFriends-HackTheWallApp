from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.FunctionInterval import Func
from panda3d.core import *

class Projectile(Actor):
    def __init__(self, app, model, start, end, shooter):
        Actor.__init__(self, model)
        self.app = app
        self.scene = app.scene
        self.start = start
        self.end = end
        self.shooter = shooter
        self.init_projectile_colors()
        self.reparentTo(self.scene)
        self.init_collision()
        self.make_shot_animation()

    def init_projectile_colors(self):
        if self.shooter == "prof":
            self.setColor(255, 0, 0)
            self.setHpr(270,0,0)
        else:
            self.setColor(0, 255, 85)
            self.setHpr(90, 0, 0)

    def init_collision(self):
        cs = CollisionSphere(0, 0, 0, 1)
        cnodePath = self.attachNewNode(CollisionNode(str(self.shooter) + "ShotCnode"))
        cnodePath.node().addSolid(cs)
        self.app.cTrav.addCollider(cnodePath, self.app.handler)

        # projectileTag = self
        # rodneyTag = self.app.rodney
        # self.app.handler.addInPattern('projectileTag-into-rodneyTag')
        # self.app.rodney.accept('projectileTag-into-rodneyTag', self.app.rodney.get_hit)
        # for prof in self.app.Profs:
        #     profTag = prof
        #     self.app.handler.addInPattern('projectileTag-into-profTag')
        #     prof.accept('projectileTag-into-profTag', prof.get_hit)

    def shoot(self):
        self.movement_animation.start()

    def get_rid_of(self):
        self.removeNode()
        self.cleanup()
        self.delete()


    def make_shot_animation(self):
        projectilePositionInterval = self.posInterval(.5, self.end, startPos = self.start)
        self.movement_animation = Sequence(projectilePositionInterval)