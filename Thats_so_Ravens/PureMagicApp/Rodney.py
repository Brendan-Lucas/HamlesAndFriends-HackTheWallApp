from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.FunctionInterval import Func
from Projectiles import Projectile
from panda3d.core import *
from pandac.PandaModules import WindowProperties


class Rodney(Actor):
    def __init__(self, app, model, rightArm=None, leftArm=None,lives=3):
        Actor.__init__(self, model)
        self.app = app
        self.scene = app.scene
        self.lives = lives
        self.last_x = 0
        self.last_y = 0
        self.charged = True
        self.block = False
        self.leftArm = leftArm
        self.rightArm = rightArm
        self.init_collision()
        self.taskMgr.add(self.mouseControlEvent, "mouseShootingEvent")

    def init_collision(self):
        cs = CollisionSphere(0, 0, 0, 1)
        cnodePath = self.attachNewNode(CollisionNode('rodneyCnode'))
        cnodePath.node().addSolid(cs)

    def shooting_animation(self):
        shooting_animation = []
        ######## TODO Change numbers to actually make a shooting animation
        shooting_animation.append(self.rightArm.hprInterval(1.0, Vec3(180, 90, 0)))
        shoot = Sequence(*shooting_animation)
        shoot.start();

    def blocking_animation(self):
        blocking_animation = []
        ######## TODO Change numbers to actually make a shooting animation
        blocking_animation.append(self.leftArm.hprInterval(1.0, Vec3(180, 90, 0)))
        block = Sequence(*blocking_animation)
        block.start()

    def charge(self):
        #self.play(charge_animation)
        self.charged = True

    def shoot(self, target):
        if self.charged:
            ###Rodney shoot animation
            self.app.rodProjectiles.append(Projectile(self.app, "PureMagicAssets/other.egg", self.getPos(), target, "rodney"))
            self.app.rodProjectiles[-1].shoot()
            self.charged = False
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

    def blocks(self):
        self.block = True
        #self.play(blocking animation)
        #self.pose(blocking animation) #### last frame for 1 second
    def unblocks(self):
        self.block = False

    def init_mouse_shooting(self):
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)

    def mouseControlEvent(self):
        curr_x = base.mouseWatcherNode.getMouseX()
        curr_y = base.mouseWatcherNode.getMouseY()
        
        if base.mouseWatcherNode.hasMouse():
            if self.last_y < 40 and curr_y():
                self.last_x = base.mouseWatcherNode.getMouseX()
                self.last_y = base.mouseWatcherNode.getMouseY()
        
        
        
        task.again
