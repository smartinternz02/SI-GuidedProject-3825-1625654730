import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "y9rotq",
        "typeId": "VIT_IBM",
        "deviceId":"1008"
    },
    "auth": {
        "token": "123456789"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

    if (m == "low"):
        print(".... Low light Intensity.....")
    elif (m == "Mid"):
        print(".... Mid light Intensity.....")
    elif (m == "High"):
        print ("......High light Intensity...")
    print()

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    water_level=random.randint(0,1000)
    low= random.randint(0, 300)
    Mid =random.randint(301, 700)
    High = random.randint(701,1000)
   
    if water_level == random.randint(0, 300):
        myData={'Water_Level_L':low}
        print(".... Low light Intensity.....")
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
        
    elif water_level == random.randint(301,700):
        myData={'Water_Level_M':Mid}
        print(".... Mid light Intensity.....")
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
        
    elif water_level == random.randint(701,1000):
        myData={'Water_Level_H':High}
        print(".... High Light Intensity.....")
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
   
 
        
client.disconnect()
