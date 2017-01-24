from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.FunctionInterval import Func
from Projectiles import Projectile
from panda3d.core import *
from direct.task import Task
from pandac.PandaModules import WindowProperties
import math
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib

SHOOT_TRIGGER = 0 #50% of the screen line
BLOCK_TRIGGER = -0.70 #15% of the screen line

class Rodney(Actor):
    def __init__(self, app, model, rightArm=None, leftArm=None, leftArmBook=None, lives=9):
        Actor.__init__(self, model)
        self.app = app
        self.scene = app.scene
        self.lives = lives
        self.last_x = 0
        self.last_y = 0
        # self.charged = True
        self.block = False
        self.setHpr(180, 0, 0)
        if leftArm: self.leftArm = self.app.loader.loadModel(leftArm)
        if rightArm: self.rightArm = self.app.loader.loadModel(rightArm)
        if leftArmBook: self.leftArmBook = self.app.loader.loadModel(leftArmBook)
        self.set_up_arms()
        self.init_collision()
        self.load_HUD()
        self.init_mouse_control_event()

    def set_up_arms(self):
        self.rightArm.reparentTo(self)
        self.rightArm.setPos(0, -1, 0.8)
        self.rightArm.setHpr(180, 0, 0)
        self.leftArm.reparentTo(self)
        self.leftArm.setPos(-10, 0, 2)
        self.leftArm.setScale(0.2, 02, 0.2)
        self.leftArm.setHpr(180, 0, 0)
        self.leftArmBook.reparentTo(self.leftArm)
        self.leftArmBook.setPos(-1, 0, -4)


    def load_HUD(self):
        self.life_image = OnscreenImage(image='Thats_so_Ravens/PureMagicApp/PureMagicAssets/life_images/rodney_lives_' + str(self.lives) + '.png', scale = (0.9, 0, 0.1),
                                        pos=(0.1,0,1.3))
        self.life_image.setTransparency(TransparencyAttrib.MAlpha)
        # self.charge_image = OnscreenImage(image='Thats_so_Ravens/PureMagicApp/PureMagicAssets/charge_on.png', scale=(0.1),
        #                                   pos=(.8, 0, 1))
        # self.charge_image.setTransparency(TransparencyAttrib.MAlpha)

    def set_life_image(self):
        self.life_image.setImage('Thats_so_Ravens/PureMagicApp/PureMagicAssets/life_images/rodney_lives_' + str(self.lives) + '.png')
        self.life_image.setTransparency(TransparencyAttrib.MAlpha)

    # def set_charge_image(self, onoff):
    #     self.charge_image.setImage('Thats_so_Ravens/PureMagicApp/PureMagicAssets/charge_' + onoff + '.png')
    #     self.charge_image.setTransparency(TransparencyAttrib.MAlpha)

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
        ######## TODO Change numbers to actually make a blocking animation
        blocking_animation.append(self.leftArm.hprInterval(1.0, Vec3(180, 90, 0)))
        block = Sequence(*blocking_animation)
        block.start()

    # def charge(self):
    #     #self.play(charge_animation)
    #     self.charged = True
    #     self.set_charge_image("on")

    def shoot(self, target):
        # if self.charged:
        #     ###Rodney shoot animation
        #     self.app.rodProjectiles.append(Projectile(self.app, "PureMagicApp/Maya_Assets/scenes/projectile.egg", self.getPos(), target, "rodney"))
        #     self.app.rodProjectiles[-1].shoot()
        #     self.charged = False
        #     self.set_charge_image("off")
        # else:
          #  self.play(uncharged animation)
        self.app.rodProjectiles.append(Projectile(self.app, "PureMagicApp/Maya_Assets/scenes/projectile.egg", self.getPos(), target, "rodney"))
        self.app.rodProjectiles[-1].shoot()

    def die(self):
        print 'die'
        self.app.game_over()
    #TODO uncoment out rodneyloosingLives
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

    def init_mouse_control_event(self):
        props = WindowProperties()
        #props.setCursorHidden(True)
        self.app.win.requestProperties(props)

    def mouse_control_event(self, task):
        if self.app.mouseWatcherNode.hasMouse():
            pres_y = self.app.mouseWatcherNode.getMouseY()
            pres_x = self.app.mouseWatcherNode.getMouseX()
            print pres_x, ', ', pres_y
            if self.block and pres_x > BLOCK_TRIGGER:
                self.unblocks()
            # TODO: add the scaling factor of the screen size so that we make the line at 0.4 * screenLength
            if self.last_y < self.app.WINDOW_SIZE_Y * SHOOT_TRIGGER and pres_y > self.app.WINDOW_SIZE_Y * SHOOT_TRIGGER:
                ratio_y = self.map(pres_y) - self.map(self.last_y)
                ratio_x = self.map(pres_x) - self.map(self.last_x)
                if ratio_y == 0: ratio_y = 0.0001
                degree = math.degrees( math.atan( ratio_x/ ratio_y ))
                self.shoot(self.scale(degree))
                #TODO: convert degree(should be between 0-180) to a number within the x constraints of profs motion
            elif pres_y < self.app.WINDOW_SIZE_Y * BLOCK_TRIGGER:
                 self.blocks()
            self.last_x = self.app.mouseWatcherNode.getMouseX()
            self.last_y = self.app.mouseWatcherNode.getMouseY()

        task.delayTime = 0.15
        return task.again

    def scale(self, degree):
        #magic numbers are adjustments with 30 = to profs y pos, 0 profs z pos.
        return (degree//2 + 12, 30, 0)

    def map(self, num):
        new_num = (num + 100) / 2
        return new_num
