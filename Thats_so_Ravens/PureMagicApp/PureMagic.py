from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import *
from Rodney import Rodney
from Projectiles import Projectile
from Profs import Prof
from direct.task import Task
from listener import Listener
# import Thats_so_Ravens.Helpers as helpers
# import Thats_so_Ravens.info as info
from pandac.PandaModules import loadPrcFileData
WINDOWSIZEX = 560
WINDOWSIZEY = 840
loadPrcFileData("", "window-title Your Title")
loadPrcFileData("", "fullscreen 0")
loadPrcFileData("", "win-size " + str(WINDOWSIZEX) + " " + str(WINDOWSIZEY))
loadPrcFileData("", "win-origin 10 10")
loadPrcFileData("", "want-directtools #t")
loadPrcFileData("", "want-tk #t")

def render_object(items, NodePath, scale=(1,1,1), pos=(1,1,-1)):
    for item in items:
        item.reparentTo(NodePath)
        item.setScale(scale)
        item.setPos(pos)

class PureMagic(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        #Ambient Light
        self.init_light()
        #backgroundColour seting to mostly red.
        self.setBackgroundColor(1,0.2,0.2,1)
        #setup scene model and camera position
        self.scene = self.init_scene_and_cam()
        #some variables:
        self.rodProjectiles = []
        self.profProjectiles = []
        self.prof_count = 0
        self.Profs = []
        self.rodney = ''
        self.init_profs()
        self.init_Rodney()
        self.taskMgr.add(self.collision_task, "handle_collisions")
        l = Listener(self)
        #start the game.
        self.nextProf()
        self.handler = CollisionHandlerQueue()
        self.traverser = CollisionTraverser('check projectiles')
        self.cTrav = self.traverser

    def init_light(self):
        ambientLight = AmbientLight("AmbLight")
        ambientLight.setColor(Vec4(1, 1, 1, 1))
        ambientLightNodePath = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNodePath)

    def init_scene_and_cam(self):
        scene = self.loader.loadModel('PureMagicAssets/classroom.egg')
        scene.reparentTo(self.render)
        scene.setPos(0, 0, 0)
        scene.setScale(1,2,2)
        #setup Camera
        self.cam.setHpr(0, -22, 0)
        self.cam.setPos(12, -80, 40)
        return scene

    def init_profModels(self):
        profModels = []
        profModels.append(self.loader.loadModel("PureMagicAssets/interimfiles/olderbrother.egg"))
        profModels.append(self.loader.loadModel("PureMagicAssets/interimfiles/ralph.egg"))
        profModels.append(self.loader.loadModel("PureMagicAssets/interimfiles/littlebrother.egg"))
        return profModels

    def init_profs(self):
        profNames=["Arod", "Emily", "Other"]
        profModels = self.init_profModels()
        for i in range(0, 3):
            self.Profs.append(Prof(self, profModels[i], (i+2), profNames[i]))

    def nextProf(self):
        ls = []
        if self.prof_count == 3:
            #TODO: load all three proffs to different locations and have them begin to attack
            render_object(self.Profs, self.scene,  pos=(-6, 8, 4.5))
            #TODO: Make proff attacking a task so that we can run it for all three.
            for Prof in self.Profs: Prof.go()
        elif self.prof_count < 3:
            ls.append(self.Profs[self.prof_count])
            render_object(ls, self.scene, pos=(-8, 8, 4.5))
            #make prof walk to centerOfRoom.
            self.Profs[self.prof_count].go()
        self.prof_count += 1

    def init_Rodney(self):
        self.rodney = Rodney(self, "PureMagicAssets/rodney_torso.egg", rightArm = "PureMagicAssets/rodney_right_arm.egg")
        self.rodney.setScale(1, 1, 1)
        self.rodney.setPos(10, -30, 10)
        self.rodney.reparentTo(self.scene)

    ##def scene.game_over

    def collision_task(self, task):
        for entry in self.handler.getEntries():
            if entry.getIntoNodePath().getName() == "rodneyCnode" and entry.getFromNodePath().getName() == "profShotCnode":
                self.rodney.get_hit()
                if self.profProjectiles:
                    self.profProjectiles[0].delete()
                    del self.profProjectiles[0]
            elif entry.getIntoNodePath().getName() == "profCnode" and entry.getFromNodePath().getName() == "rodneyShotCnode":
                self.Profs[self.prof_count-1].get_hit()
                if self.rodProjectiles:
                    self.rodProjectiles[0].delete()
                    del self.rodProjectiles[0]
            elif entry.getIntoNodePath().getName() == "wall_plane":
                if self.rodProjectiles:
                    self.rodProjectiles[0].delete()
                    del self.rodProjectiles[0]
            self.handler.clear_entries()
        return Task.cont

pureMagic = PureMagic()
pureMagic.run()
