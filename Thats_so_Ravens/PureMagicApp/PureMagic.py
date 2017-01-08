from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
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
            self.render_object(self.Profs)
        else:
            self.render_object(self.Profs[self.prof_count])

        #make prof walk to scenterofRoom.
        self.Profs[self.prof_count].start_attacking()
        self.prof_count += 1

    def run(self):
        self.prof_count = 0
        self.scene.reparentTo(self.render)
        #infoBoxExplainingStuff
        #while self.prof_count < 4:
            #self.rodney.run()
            #self.nextProf()

    ##def scene.game_over

class Prof(Actor):
    def __init__(self, scene, model, lives):
        Actor.__init__(model)
        self.scene = scene
        self.lives = lives

    def attack(self, shot_frequency):
        #self.loop(movement_sequence)
        self.shoot(shot_frequency)

    def enter(self):
        #self.play(enter_animation)
        #self.play(shit_talk)
        x = 1

    def get_hit(self):
        self.lives -= 1
        #self.play(get_hit_animation)
        if self.lives == 0:
            self.die()

    def shoot(self):
        x = 1
        ###### RANDOM LOOP OF SHOOTING
            ### shoot

    def die(self):
        #self.play(death_animation)
        self.removeNode()

class Rodney(Actor):
    def __init__(self, scene, model, lives):
        Actor.__init__(model)
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

pureMagic = PureMagic()
pureMagic.run()
