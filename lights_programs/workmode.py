from EasyTuya import TuyaAPI
from EasyTuya.devices import Lights

client_id=""    # The client_id can be obtained from the project created in cloud
client_key=""   # The client key can also be obtained in a similar manner
device_id=""    # The device id can be obtained from adding a device to the cloud project

api = TuyaAPI(client-id, client_key)
l1 = Lights.Light(device_id, "Light 1")
api.addDevices([l1], "LIGHTS")

toDo=input()

if toDo == "white":
    api.sendCommands("LIGHTS", Lights.workModeCommand("white"))
elif toDo == "color":
    api.sendCommands("LIGHTS", Lights.workModeCommand("colour"))

# Other modes can be added based on your device compactinility like scene, music, etc