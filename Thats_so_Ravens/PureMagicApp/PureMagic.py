from direct.showbae.ShowBase import ShowBase
import info
import Thats_so_Ravens.Helpers as helpers
import Thats_so_Ravens.info as info

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
        self.initProfModels()
        #self.Profs = []
        #self.init_profs()
        #self.rodney = Rodney(self.scene)
        #position camera;

    def init_profModels(self):
        self.profModels.append(self.loader.loadModel("PureMagicAssets/A_Rod_Mod.egg"))
        self.profModels.append(self.loader.loadModel("PureMagicAssets/Emily.egg"))
        self.profModels.append(self.loader.loadModel("PureMagicAssets/other.egg"))

    def init_profs(self):
        for i in range(0, 4, step=1):
            self.Profs.append(Prof(self.scene, self.profModels[i], (i+2)))

    def render_object(items, NodePath, scale, pos=(1,1,-1)):
        for item in items:
            item.reparentTo(NodePath)
            if scale: item.setScale(scale)
            item.setPos(pos)

    def nextProf(self):
        if self.prof_count == 3:
            render_object(self.Profs)
        else:
            render_object(self.Profs[prof_count])

        #make prof walk to scenterofRoom.
        self.Profs[prof_count].start_attacking()
        self.prof_count+=1

    def run(self):
        self.prof_count=0
        self.scene.reparentTo(self.render)
        #infoBoxExplainingStuff
        #while self.prof_count < 4:
            #self.rodney.run()
            #self.nextProf()

pureMagic = PureMagic()
pureMagic.run()
