from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.FunctionInterval import Func
from Projectiles import Projectile
from panda3d.core import *

class Prof(Actor):
    def __init__(self, app, model, lives, name):
        Actor.__init__(self, model)
        # self.reparentTo(scene)

        self.app = app
        self.name = name
        self.scene = self.app.scene
        self.lives = lives
        self.prof_name = name
        self.init_collision()
        self.init_collision_plane()
        self.setup_life_bar()

    def setup_life_bar(self):
        self.life_bar = self.app.loader.loadModel("PureMagicApp/PureMagicAssets/other.egg")
        self.life_bar.reparentTo(self)
        self.life_bar.setPos(0, 0, 3)
        self.set_life_bar()


    def set_life_bar(self):
        if self.lives == 1:
            self.life_bar.setColor(255, 0, 0)
        elif self.lives == 2:
            self.life_bar.setColor(255, 255, 0)
        elif self.lives == 3:
            self.life_bar.setColor(0, 255, 0)
        elif self.lives == 4:
            self.life_bar.setColor(0, 0, 255)
        self.life_bar.setScale(self.lives*.1, .1, .1)


    def walkin(self):
        self.reparentTo(self.scene)
        self.make_move_animation()

    def go(self):
        self.walkin()
        self.attack()

    def attack(self):
        self.prof_movement.loop()

    def get_hit(self):
        self.lives -= 1
        #self.play(get_hit_animation)
        if self.lives == 0:
            self.die()
        self.set_life_bar()

    # def shooting_pattern(self):
    #     self.shoot()

    def shoot(self, start, end):
        #prof shoot animation
        self.app.profProjectiles.append(Projectile(self.app, "PureMagicApp/Maya_Assets/scenes/projectile.egg", start, end, "prof"))
        self.app.profProjectiles[-1].shoot()

        ###### RANDOM LOOP OF SHOOTING
            ### shoot

    def die(self):
        #self.play(death_animation)
        self.detachNode()
        self.prof_movement.finish()
        self.app.nextProf()

    def make_move_animation(self):
        def addTupple(x, y):
            z = []
            for i in range(len(x)):
                z.append(x[i] + y[i])
            return tuple(z)

        distance = 25
        x = distance/6
        start = location = self.getPos()
        profPositionIntervals = []
        if self.prof_name == "Arod":
            speed = 5
            i = 1
            while i <= 6:
                profPositionIntervals.append(self.posInterval(5/speed, Point3(addTupple(location, (1.3 * x, 0, 0))), startPos=location))
                location = addTupple(location, (1.3 * x, 0, 0))
                profPositionIntervals.append(Func(self.shoot, Point3(location), self.app.rodney.getPos))
                i += 1
            while i >= 1:
                profPositionIntervals.append(self.posInterval(5/speed, Point3(addTupple(location, (-1.3 * x, 0, 0))), startPos=location))
                location = addTupple(location, (-1.3 * x, 0, 0))
                profPositionIntervals.append(Func(self.shoot, Point3(location), self.app.rodney.getPos))
                i -= 1
        elif self.prof_name == "Emily":
            speed = 1
            self.setScale(0.5)
            self.life_bar.setPos(0, 0, 7)
            for i in range(0, 3):
                profPositionIntervals.append(self.posInterval(2/speed, Point3(addTupple(location, (1*x, -2*x, 0))),
                                                     startPos=location))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (2*x, -2*x, 0))), self.app.rodney.getPos))
                profPositionIntervals.append(self.posInterval(2/speed, Point3(addTupple(location, (4*x, 0, 0))),
                                                     startPos=addTupple(location, (2*x, -2*x, 0))))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (4*x, 0, 0))), self.app.rodney.getPos))
                profPositionIntervals.append(self.posInterval(1/speed, Point3(addTupple(location, (3*x, -1*x, 0))),
                                                     startPos=addTupple(location, (4*x, 0, 0))))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (3*x, -1*x, 0))), self.app.rodney.getPos))

                profPositionIntervals.append(self.posInterval(1/speed, Point3(addTupple(location, (2*x, 0, 0))),
                                                     startPos=addTupple(location, (3*x, -1*x, 0))))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (2*x, 0, 0))), self.app.rodney.getPos))
                location = addTupple(location, (2*x, 0, 0))
            profPositionIntervals.append(self.posInterval(4/speed, Point3(start), startPos=location))
        elif self.prof_name == "Other":
            speed = 0.5
            for i in range(0,5):
                profPositionIntervals.append(self.posInterval(.5/speed, Point3(addTupple(location, (1.7*x, 0, 0))), startPos=location),)
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (1.7*x, 0, 0))), self.app.rodney.getPos))
                profPositionIntervals.append(self.posInterval(.25/speed, Point3(addTupple(location, (0.85*x, 0, 0))), startPos=addTupple(location, (2*x, 0, 0))))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (0.85*x, 0, 0))), self.app.rodney.getPos))
                location = addTupple(location, (1.7*x, 0, 0))
            for i in range(0,5):
                profPositionIntervals.append(self.posInterval(.5/speed, Point3(addTupple(location, (-1.7*x, 0, 0))), startPos=location))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (-1.7*x, 0, 0))), self.app.rodney.getPos))
                profPositionIntervals.append(self.posInterval(.25/speed, Point3(addTupple(location, (-0.85*x, 0, 0))),
                                                              startPos=addTupple(location, (-1.7*x, 0, 0))))
                profPositionIntervals.append(Func(self.shoot, Point3(addTupple(location, (-0.85*x, 0, 0))), self.app.rodney.getPos))

                location = addTupple(location, (-1.7*x, 0, 0))
            # profPositionIntervals.append(self.posInterval(3, Point3(start), startPos=location))

        # for action in profPositionIntervals:

        self.prof_movement = Sequence(*profPositionIntervals, name="prof_movement" + str(self.name))

    def init_collision(self):
        cs = CollisionSphere(0, 0, 0, 1)
        cnodePath = self.attachNewNode(CollisionNode('profCnode'))
        cnodePath.node().addSolid(cs)

    def init_collision_plane(self):
        cp = CollisionPlane(Plane(Vec3(0, -1, 0), Point3(0, 1, 0)))
        cnodePath = self.attachNewNode(CollisionNode('wall_plane'))
        cnodePath.node().addSolid(cp)
