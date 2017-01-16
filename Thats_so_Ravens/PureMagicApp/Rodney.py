from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.FunctionInterval import Func
from Projectiles import Projectile
from panda3d.core import *
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib


class Rodney(Actor):
    def __init__(self, app, model, rightArm=None, leftArm=None,lives=3):
        Actor.__init__(self, model)
        self.app = app
        self.scene = app.scene
        self.lives = lives
        self.charged = True
        self.block = False
        self.setHpr(180, 0, 0)
        if leftArm: self.leftArm = self.app.loader.loadModel(leftArm)
        if rightArm: self.rightArm = self.app.loader.loadModel(rightArm)
        self.set_up_arms()
        self.init_collision()
        self.load_HUD()

    def set_up_arms(self):
        self.rightArm.reparentTo(self)
        self.rightArm.setPos(0, -1, 0.8)
        self.rightArm.setHpr(180, 0, 0)
        # self.leftArm.reparentTo(self)
        # self.lefttArm.setPos(-5, 0, 2)

    def load_HUD(self):
        self.life_image = OnscreenImage(image='PureMagicAssets/rodney_lives_' + str(self.lives) + '.png', scale=(0.1),
                                        pos=(.8, 0, 1.3))
        self.life_image.setTransparency(TransparencyAttrib.MAlpha)
        self.charge_image = OnscreenImage(image='PureMagicAssets/charge_on.png', scale=(0.1),
                                          pos=(.8, 0, 1))
        self.charge_image.setTransparency(TransparencyAttrib.MAlpha)

    def set_life_image(self):
        self.life_image.setImage('PureMagicAssets/rodney_lives_' + str(self.lives) + '.png')
        self.life_image.setTransparency(TransparencyAttrib.MAlpha)

    def set_charge_image(self, onoff):
        self.charge_image.setImage('PureMagicAssets/charge_' + onoff + '.png')
        self.charge_image.setTransparency(TransparencyAttrib.MAlpha)

    # def set_charge_image(self):

    def init_collision(self):
        cs = CollisionSphere(0, 0, 0, 1)
        cnodePath = self.attachNewNode(CollisionNode('rodneyCnode'))
        cnodePath.node().addSolid(cs)

    def shooting_animation(self):
        shooting_animation = []
        ######## TODO Change numbers to actually make a shooting animation
        shooting_animation.append(self.rightArm.hprInterval(1.0, Vec3(180, 90, 0)))
        shoot = Sequence(*shooting_animation)
        shoot.start()

    def blocking_animation(self):
        blocking_animation = []
        ######## TODO Change numbers to actually make a shooting animation
        blocking_animation.append(self.leftArm.hprInterval(1.0, Vec3(180, 90, 0)))
        block = Sequence(*blocking_animation)
        block.start()

    def charge(self):
        #self.play(charge_animation)
        self.charged = True
        self.set_charge_image("on")

    def shoot(self, target):
        if self.charged:
            ###Rodney shoot animation
            self.app.rodProjectiles.append(Projectile(self.app, "PureMagicAssets/other.egg", self.getPos(), target, "rodney"))
            self.app.rodProjectiles[-1].shoot()
            self.charged = False
            self.set_charge_image("off")
        # else:
          #  self.play(uncharged animation)

    def die(self):
        print 'die'
        self.scene.game_over()

    def get_hit(self):
        if not self.block:
            self.lives -= 1
            #   self.play(get hit animation)
            if self.lives == 0:
                self.die()
            else:
                self.set_life_image()


    def blocks(self):
        self.block = True
        #self.play(blocking animation)
        #self.pose(blocking animation) #### last frame for 1 second
    def unblocks(self):
        self.block = False
