from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpPosInterval
from panda3d.core import Point3
# import Thats_so_Ravens.Helpers as helpers
# import Thats_so_Ravens.info as info

class PureMagic(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.prof_count = 0;
        #load model
        self.scene = self.loader.loadModel("PureMagicAssets/Gym.egg")
        #reparent scene to render
        self.scene.reparentTo(self.render)
        #set scale and positon of the model/scene
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        self.profModels = []
        self.init_profModels()
        #self.Profs = []
        #self.init_profs()
        #self.rodney = Rodney(self.scene)
        #position camera;

    def init_profModels(self):
        self.profModels.append(self.loader.loadModel("PureMagicAssets/A_Rod_Mod.egg"))
        self.profModels.append(self.loader.loadModel("PureMagicAssets/Emily.egg"))
        self.profModels.append(self.loader.loadModel("PureMagicAssets/other.egg"))

    def init_profNames(self):
        self.profNames.append("Arod")
        self.profNames.append("Emily")
        self.profNames.append("Other")

    def init_profs(self):
        for i in range(0, 3):
            self.Profs.append(Prof(self.render, self.profModels[i], (i+2), self.profNames[i]))

    def render_object(items, NodePath, scale, pos=(1,1,-1)):
        for item in items:
            item.reparentTo(NodePath)
            if scale: item.setScale(scale)
            item.setPos(pos)

    def nextProf(self):
        if self.prof_count == 3:
            self.render_object(self.Profs)
        else:
            self.render_object(self.Profs[self.prof_count])

        #make prof walk to scenterofRoom.
        self.Profs[self.prof_count].start_attacking()
        self.prof_count += 1

    # def run(self):
    #     self.prof_count = 0
    #     self.scene.reparentTo(self.render)
    #     #infoBoxExplainingStuff
    #     #while self.prof_count < 4:
    #         #self.rodney.run()
    #         #self.nextProf()

    ##def scene.game_over

class Prof(Actor):
    def __init__(self, scene, model, lives, name):
        Actor.__init__(self, model)
        self.reparentTo(scene)
        self.setScale(0.03,0.03,0.03)
        self.scene = scene
        self.setPos(0, 0, 0)
        self.lives = lives
        self.prof_name = name
        self.make_move_animation()

    def attack(self, shot_frequency = 1):
        self.prof_movement.loop()
        self.shooting_pattern()

    def enter(self):
        #self.play(enter_animation)
        #self.play(shit_talk)
        return

    def get_hit(self):
        self.lives -= 1
        #self.play(get_hit_animation)
        if self.lives == 0:
            self.die()

    def shooting_pattern(self):
        self.shoot()

    def shoot(self):
        #prof shoot animation
        Projectile(self.scene, "PureMagicAssets/other.egg", self.getPos(), self.scene.rodney.getPos())
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
            self.prof_movement = Sequence(*profPositionIntervals, name="movement_animation")
        elif self.prof_name == "Emily":
            for i in range(0, 3):
                profPositionIntervals.append(self.posInterval(2, Point3(addTupple(location, (20, -20, 0))),
                                                     startPos=location))
                profPositionIntervals.append(self.posInterval(2, Point3(addTupple(location, (40, 0, 0))),
                                                     startPos=addTupple(location, (20, -20, 0))))
                profPositionIntervals.append(self.posInterval(1, Point3(addTupple(location, (30, -10, 0))),
                                                     startPos=addTupple(location, (40, 0, 0))))
                profPositionIntervals.append(self.posInterval(1, Point3(addTupple(location, (20, 0, 0))),
                                                     startPos=addTupple(location, (30, -10, 0))))
                location = addTupple(location, (20, 0, 0))
            profPositionIntervals.append(self.posInterval(4, Point3(start), startPos=location))
        elif self.prof_name == "Other":
            for i in range(0,5):
                profPositionIntervals.append(self.posInterval(.5, Point3(addTupple(location, (20, 0, 0))), startPos=location))
                profPositionIntervals.append(self.posInterval(.25, Point3(addTupple(location, (10, 0, 0))), startPos=addTupple(location, (20, 0, 0))))
                location = addTupple(location, (20, 0, 0))
            for i in range(0,5):
                profPositionIntervals.append(self.posInterval(.5, Point3(addTupple(location, (-20, 0, 0))), startPos=location))
                profPositionIntervals.append(self.posInterval(.25, Point3(addTupple(location, (-10, 0, 0))),
                                                              startPos=addTupple(location, (-20, 0, 0))))
                location = addTupple(location, (-20, 0, 0))
            # profPositionIntervals.append(self.posInterval(3, Point3(start), startPos=location))

        self.prof_movement = Sequence(*profPositionIntervals, name="prof_movement")


class Rodney(Actor):
    def __init__(self, scene, model, lives):
        Actor.__init__(self, model)
        self.scene = scene
        self.lives = lives
        self.charged = False
        self.block = True

    def charge(self):
        #self.play(charge_animation)
        self.charged = True

    def shoot(self, target):
        if self.charge:
            ###Rodney shoot animation
            Projectile(self.scene, "PureMagicAssets/other.egg", self.getPos(), target)
            self.charged = False
        # else:
          #  self.play(uncharged animation)

    def get_hit(self):
        if not self.block:
            self.lives -= 1
         #   self.play(get hit animation)
            if self.lives == 0:
                self.die

    def die(self):
        #self.play(death_animation)
        self.scene.game_over()

    def block(self):
        self.block = True
        #self.play(blocking animation)
        #self.pose(blocking animation) #### last frame for 1 second
        self.block = False

class Projectile(Actor):
    def __init__(self, scene, model, start, end):
        Actor.__init__(self, model)
        self.scene = scene
        self.start = start
        self.end = end
        self.reparentTo(self.scene)
        self.make_move_animation()

    def shoot(self):
        self.movement_animation.loop()

    def make_move_animation(self):
        projectilePositionInterval = self.posInterval(5, Point3(self.end), startPos = self.start)
        self.movement_animation = Sequence(projectilePositionInterval, name = "movement_animation")

    def delete(self):
        self.remove_node()

pureMagic = PureMagic()
pureMagic.run()
