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

class PureMagic(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.prof_count = 0;
        #load model
        self.scene = self.render
        self.test_function()
        self.taskMgr.add(self.collision_task, "handle_collisions")
        l = Listener(self)
        # self.scene = self.loader.loadModel("PureMagicAssets/Gym.egg")
        # #reparent scene to render
        # self.scene.reparentTo(self.render)
        # #set scale and positon of the model/scene
        # self.scene.setScale(0.25, 0.25, 0.25)
        # self.scene.setPos(-8, 42, 0)
        # self.profModels = []
        # self.init_profModels()
        # #self.Profs = []
        #self.init_profs()
        #self.rodney = Rodney(self.scene)
        #position camera;

    def test_function(self):
        self.rodProjectiles = []
        self.profProjectiles = []

        self.rodney = Rodney(self, "PureMagicAssets/Emily.egg")
        self.rodney.setScale(0.1, 0.1, 0.1)
        self.rodney.setPos(0, 20, 0)
        self.rodney.reparentTo(self.render)

        self.Profs = []
        self.scene = self.render
        self.init_profs()

        self.Profs[1].go()

        self.handler = CollisionHandlerQueue()
        self.traverser = CollisionTraverser('check projectiles')
        self.cTrav = self.traverser

    def shoot_task(self, task):
        return


    def collision_task(self, task):
        for entry in self.handler.getEntries():
            if entry.getIntoNodePath().getName() == "rodneyCnode" and entry.getFromNodePath().getName() == "profShotCnode":
                self.rodney.get_hit()
                self.profProjectiles[0].delete()
                del self.profProjectiles[0]
            elif entry.getIntoNodePath().getName() == "profCnode" and entry.getFromNodePath().getName() == "rodneyShotCnode":
                self.Profs[self.active_prof].get_hit()
                self.rodProjectiles[0].delete()
                del self.rodProjectiles[0]
            elif entry.getIntoNodePath().getName() == "wall_plane":
                self.rodProjectiles[0].delete()
                del self.rodProjectiles[0]
            self.handler.clear_entries()
        return Task.cont

    def init_profModels(self):
        profModels = []
        profModels.append(self.loader.loadModel("PureMagicAssets/A_Rod_Mod.egg"))
        profModels.append(self.loader.loadModel("PureMagicAssets/Emily.egg"))
        profModels.append(self.loader.loadModel("PureMagicAssets/other.egg"))
        return profModels

    def init_profNames(self):
        profNames = []
        profNames.append("Arod")
        profNames.append("Emily")
        profNames.append("Other")
        return profNames


    def init_profs(self):
        profNames = self.init_profNames()
        profModels = self.init_profModels()
        for i in range(0, 3):
            self.Profs.append(Prof(self, profModels[i], (i+2), profNames[i]))
        self.active_prof = 0

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

pureMagic = PureMagic()
pureMagic.run()
