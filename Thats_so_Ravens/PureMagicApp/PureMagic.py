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
        self.Profs = []
        #TODO: multiThread Rodney
        #self.rodney = Rodney(self.scene)
        self.init_profs()
        #TODO: Decide what happens after profs die.
        #position camera;

    def init_profModels(self):
        self.profModels.append(self.loader.loadModel("PureMagicAssets/A_Rod_Mod.egg"))
        self.profModels.append(self.loader.loadModel("PureMagicAssets/Emily.egg"))
        self.profModels.append(self.loader.loadModel("PureMagicAssets/other.egg"))

    def init_profs(self):
        profNames=["Arod", "Emily", "Other"]
        for i in range(0, 4):
            self.Profs.append(Prof(self.scene, self.profModels[i], (i+2), profNames[i], 1, self))

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
        self.Profs[self.prof_count].attack()
        self.prof_count += 1
    ##def scene.game_over

class Prof(Actor):
    def __init__(self, scene, model, lives, name, attack_speed, pureApp):
        Actor.__init__(self, model)
        self.scene = scene
        self.lives = lives
        self.prof_name = name
        self.app = pureApp
        self.attack_speed = attack_speed
        self.make_move_animation()

    def attack(self):
        self.movement_animation.loop()
        self.shoot()

    def enter(self):
        #self.play(enter_animation)
        #self.play(shit_talk)
        return

    def get_hit(self):
        self.lives -= 1
        #self.play(get_hit_animation)
        if self.lives == 0:
            self.die()

    def shoot(self):
        #self.attack_speed
        return
        ###### RANDOM LOOP OF SHOOTING
            ### shoot

    def die(self):
        #self.play(death_animation)
        self.removeNode()
        self.app.nextProf()

    def make_move_animation(self):
        def addTupple(x, y):
            z = []
            for i in range(len(x)):
                z.append(x[i] + y[i])
            return tuple(z)

        if self.prof_name == "Arod":
            profPositionInterval2 = self.posInterval(5, Point3(self.start), startPos = self.end)
            profPositionInterval1 = self.posInterval(5, Point3(self.end), startPos = self.start)
            self.movement_animation = Sequence(profPositionInterval1, profPositionInterval2, name="movement_animation")
        if self.prof_name == "Emily":
            start = self.getPos()
            profPositionIntervals = []
            for i in range(0, 3):
                profPositionIntervals.append(self.posInterval(2, Point3(addTupple(start, (2, 2, 0))),
                                                     startPos=start))
                profPositionIntervals.append(self.posInterval(2, Point3(addTupple(start, (4, 0, 0))),
                                                     startPos=addTupple(start, (2, 2, 0))))
                profPositionIntervals.append(self.posInterval(1, Point3(addTupple(start, (3, 1, 0))),
                                                     startPos=addTupple(start, (4, 0, 0))))
                profPositionIntervals.append(self.posInterval(1, Point3(addTupple(start, (2, 0, 0))),
                                                     startPos=addTupple(start, (3, 1, 0))))
                start = addTupple(start, (2, 0, 0))
            self.scene.getParent().prof_movement = Sequence(profPositionIntervals[0], profPositionIntervals[1], profPositionIntervals[2], profPositionIntervals[3], profPositionIntervals[4], profPositionIntervals[5], profPositionIntervals[6], profPositionIntervals[7], profPositionIntervals[8], profPositionIntervals[9], profPositionIntervals[10], profPositionIntervals[11], name="prof_movement")

        if self.prof_name == "Other":
            return

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

    def shoot(self, direction):
        if self.charge:
            #### CREATE PROJECTILE AND FIRE IT IN THE DIRECTION THAT WE WANT IT TO GO
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

class Projectiles(Actor):
    def __init__(self, scene, model, start, end):
        Actor.__init__(self, model)
        self.scene = scene
        self.start = start
        self.end = end
        self.movement_animation = self.make_move_animation()
        self.movement_animation.loop()

    def make_move_animation(self):
        return self.LerpPosInterval(13, Point3(self.end), startPos = self.start)

pureMagic = PureMagic()
pureMagic.run()
