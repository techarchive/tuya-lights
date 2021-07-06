# tuya-lights

This project is developed using Tuya SDK, which enables you to quickly develop smart devices, branded APP, cloud development project, etc.

For more information, please check Tuya Developer Click and Connect Challenge https://pages.tuya.com/develop/ClickAndConnect_TuyaDeveloper?_source=e9684c7ca6b31e7221c8420f5af94631



<h3>Documentation:</h3>
  
See the full documentation: <a href="https://github.com/techarchive/tuya-lights/blob/main/docs/Lights.html">here</a>
<br>
  
<h3>Installation:</h3>
 
```
  pip install EasyTuya
```

<h3>Requirements:</h3>

  <a href="https://pypi.org/project/pycryptodome/">pycryptodome</a>

 
  <h3>Demo Code:</h3>
  
  ```Python
  from EasyTuya import TuyaAPI
from EasyTuya.devices import Lights

client_id=""    # The client_id can be obtained from the project created in cloud
client_key=""   # The client key can also be obtained in a similar manner
device_id=""    # The device id can be obtained from adding a device to the cloud project

api = TuyaAPI(client-id, client_key)
l1 = Lights.Light(device_id, "Light 1")
api.addDevices([l1], "LIGHTS")

toDo=input()

if toDo == "on":
    api.sendCommands("LIGHTS", Lights.onCommand())
elif toDo == "off":
    api.sendCommands("LIGHTS", Lights.offCommand())
        
        
        
# other functions are included in the folder lights_program, and see the below list for the functions available.
  ```
  
  <h3>Other Functions:</h3>
  1. on, off <br>
  2. workmode <br>
  3. color <br>
  4. toggle <br>
  5. brightness <br>
  6. scene <br>
  7. list of devices <br>
  <br>
  
  <h3>Steps to use the API:</h3>
  
  #### Step 1: CLIENT_ID and SECRET_KEY
- Register or Login on <a href="https://auth.tuya.com" target="_blanck">Tuya</a>.
1. Create a cloud development project <a href="https://iot.tuya.com/cloud" target="_blanck">Cloud -> Project</a>.
2. After successful creation, you will receive the **Client ID** and **Secret Key**.


#### Step 2: DEVICE_ID
1. Install **Tuya Smart** app or **Smart Life** app on your mobile phone.
2. Go to <a href="https://iot.tuya.com/cloud/appinfo/cappId/device" target="_blanck">Cloud -> Link Devices</a> page.
3. Selecting a tab **Link Devices by App Account**.
4. Click **Add App Account** and scan the QR code with **Tuya Smart** app or **Smart Life** app.
5. Now you can go to devices <a href="https://iot.tuya.com/cloud/appinfo/cappId/deviceList" target="_blanck">Cloud -> Device List</a> and copy **Device ID**.
    * Notes: Try to select a your region if devices are not displayed.


#### Step 3: Request access to API calls
Go to <a href="https://iot.tuya.com/cloud/appinfo/cappId/setting" target="_blanck">Cloud -> API Group</a> and enable **Authorization management**, **Device Management** and **Device Control**.
<br>

 <h3>Note:</h3>
 Get the client_id, client_key, device_id in order to use the project.
 
