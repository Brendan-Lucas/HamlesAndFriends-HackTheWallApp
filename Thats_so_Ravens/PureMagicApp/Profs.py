from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.FunctionInterval import Func
from Projectiles import Projectile
from panda3d.core import *

class Prof(Actor):
    def __init__(self, app, model, lives, name):
        Actor.__init__(self, model)
        # self.reparentTo(scene)
        self.setScale(0.03,0.03,0.03)
        self.app = app
        self.scene = self.app.scene
        self.lives = lives
        self.prof_name = name
        self.init_collision()
        self.accept('projectileTag-into-profTag', self.get_hit)


    def walkin(self):
        self.setPos(0, 200, 0)
        self.reparentTo(self.scene)
        self.make_move_animation()

    def go(self):
        self.walkin()
        self.attack()


    def attack(self, shot_frequency = 1):
        self.prof_movement.loop()
        # self.shooting_pattern()

    def enter(self):
        #self.play(enter_animation)
        #self.play(shit_talk)
        return

    def get_hit(self):
        self.lives -= 1
        #self.play(get_hit_animation)
        if self.lives == 0:
            self.die()

    # def shooting_pattern(self):
    #     self.shoot()

    def shoot(self, start, end):
        #prof shoot animation
        self.app.Projectiles.append(Projectile(self.app, "PureMagicAssets/other.egg", start, end))
        self.app.Projectiles[-1].shoot()

        ###### RANDOM LOOP OF SHOOTING
            ### shoot

    def die(self):
        #self.play(death_animation)
        self.removeNode()

    def make_move_animation(self):
        def addTupple(x, y):
            z = []
            for i in range(len(x)):
                z.append(x[i] + y[i])
            return tuple(z)

        start = location = self.getPos()
        profPositionIntervals = []
        if self.prof_name == "Arod":
            profPositionIntervals.append(self.posInterval(5, Point3(start), startPos = (60, 0, 0)))
            profPositionIntervals.append(self.posInterval(5, Point3(60, 0, 0), startPos = start))
        elif self.prof_name == "Emily":
            for i in range(0, 3):
                profPositionIntervals.append(self.posInterval(2, Point3(addTupple(location, (20, -20, 0))),
                                                     startPos=location))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (20, -20, 0))), self.app.rodney.getPos))
                profPositionIntervals.append(self.posInterval(2, Point3(addTupple(location, (40, 0, 0))),
                                                     startPos=addTupple(location, (20, -20, 0))))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (40, 0, 0))), self.app.rodney.getPos))
                profPositionIntervals.append(self.posInterval(1, Point3(addTupple(location, (30, -10, 0))),
                                                     startPos=addTupple(location, (40, 0, 0))))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (30, -10, 0))), self.app.rodney.getPos))

                profPositionIntervals.append(self.posInterval(1, Point3(addTupple(location, (20, 0, 0))),
                                                     startPos=addTupple(location, (30, -10, 0))))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (20, 0, 0))), self.app.rodney.getPos))
                location = addTupple(location, (20, 0, 0))
            profPositionIntervals.append(self.posInterval(4, Point3(start), startPos=location))
        elif self.prof_name == "Other":
            for i in range(0,5):
                profPositionIntervals.append(self.posInterval(.5, Point3(addTupple(location, (20, 0, 0))), startPos=location),)
                profPositionIntervals.append(self.posInterval(.25, Point3(addTupple(location, (10, 0, 0))), startPos=addTupple(location, (20, 0, 0))))
                location = addTupple(location, (20, 0, 0))
            for i in range(0,5):
                profPositionIntervals.append(self.posInterval(.5, Point3(addTupple(location, (-20, 0, 0))), startPos=location))
                profPositionIntervals.append(self.posInterval(.25, Point3(addTupple(location, (-10, 0, 0))),
                                                              startPos=addTupple(location, (-20, 0, 0))))
                location = addTupple(location, (-20, 0, 0))
            # profPositionIntervals.append(self.posInterval(3, Point3(start), startPos=location))

        # for action in profPositionIntervals:

        self.prof_movement = Sequence(*profPositionIntervals, name="prof_movement")

    def init_collision(self):
        cs = CollisionSphere(0, 0, 0, 1)
        cnodePath = self.attachNewNode(CollisionNode('profCnode'))
        cnodePath.node().addSolid(cs)
