from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.actor.Actor import Actor
from panda3d.core import AmbientLight
from panda3d.core import Vec4
from panda3d.core import DirectionalLight

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        self.disableMouse()
        self.environment = loader.loadModel("models/misc/Environment/environment") 
        self.environment.reparentTo(render)

        self.tempActor=Actor("models/panda", {"walk": "models/panda-walk"})
        self.tempActor.reparentTo(render)
        self.tempActor.setPos(0, 7, 0)
        self.tempActor.setScale(0.05, 0.05, 0.05)
        self.tempActor.loop("walk")
        #camera control
        self.camera.setPos(0,0,32)
        self.camera.setP(-90)

        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(self.ambientLightNodePath)

        mainLight = DirectionalLight("main light")
        self.mainLightNodePath = render.attachNewNode(mainLight)
        # turn it 45 degrees, tilt down 45 degrees
        self.mainLightNodePath.setHpr(45,-45,0)
        render.setLight(self.mainLightNodePath)

        render.setShaderAuto()

        self.keyMap = {
        "up" : False,
        "down" : False,
        "left" : False,
        "right" : False,
        "shoot" : False
        }
        def updateKeyMap(self, controlName, controlState):
            self.keyMap[controlName] = controlState
            print (controlName, "set to", controlState)

        self.accept("w", self.updateKeyMap, ["up", True])
        self.accept("w-up", self.updateKeyMap, ["up", False])
        self.accept("s", self.updateKeyMap, ["down", True])
        self.accept("s-up", self.updateKeyMap, ["down", False])
        self.accept("a", self.updateKeyMap, ["left", True])
        self.accept("a-up", self.updateKeyMap, ["left", False])
        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])
        self.accept("mouse1", self.updateKeyMap, ["shoot", True])
        self.accept("mouse1-up", self.updateKeyMap, ["shoot", False])

app = MyApp()
app.run()