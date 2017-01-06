from direct.showbae.ShowBase import ShowBase
import info
import Thats_so_Ravens.Helpers as helpers
import Thats_so_Ravens.info as info

class PureMagic(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        #load model
        #self.scene = self.loader.loadModel("modelPath")
        #reparent scene to render
        #self.scene.reparentTo(self.render)
        #set scale and positon of the model/scene
        #self.scene.setScale(0.25, 0.25, 0.25)
        #self.scene.setPos(-8, 42, 0)
        self.Profs[] = self.init_profs()
        self.rodney = Rodney()
        #position camera;

    def init_profs(self):
        for i in range(0, 4, step=1):
            self.Profs[i]= Prof(self.profModels[i])
            

    def run(self):
