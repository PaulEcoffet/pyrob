#%% Init
from pyroborobo import Pyroborobo, PyController, PyWorldModel
import numpy as np
mode = 1

#%%
if mode == 0:
#%%

    # rob = Pyroborobo(propertiesfile, worldobserver, controller, worldModel, agentobserver, conf_dict_override)

    # Pour l’instant, tous les arguments sont obligatoires même si mis à None
    rob = Pyroborobo("config/useless/template_wander_smallrobots.properties", None, None, None, None,
                     {'gDisplayMode': "0"})

    rob.start()

    rob.update(1000)

    # Crash pour une raison inconnue
    rob.close()
#%%
else:
#%%
    class Controller(PyController):

        def reset(self):
            self.wm = self.getWorldModel()
            self.wm.rotspeed = 0
            self.wm.speed = 0

        def step(self):
            self.wm = self.getWorldModel()
            dists = self.wm.getCameraSensorsDist()
            if np.any(dists[0:4] < 0.5):
                self.wm.rotspeed = 20
                self.wm.speed = 0
            else:
                self.wm.rotspeed = 0
                self.wm.speed = 2


    rob = Pyroborobo('config/useless/template_wander_smallrobots.properties', None, Controller, None, None,
                     {'gDisplayMode': "0"})

    rob.start()

    rob.update(1000)

    # Crash pour une raison inconnue avec le close
    rob.close()
