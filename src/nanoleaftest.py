from nanoleafapi import discovery, Nanoleaf
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE

#nanoleaf_dict = discovery.discover_devices()

#print(nanoleaf_dict)
auth_token = "yD3RlM2LKIBAUJXxILjnjeBIKtxLGroB"
ip = "192.168.3.34"
effects = ['Color Burst', 'Falling Whites', 'Fireworks', 'Flames', 'Forest', 'Inner Peace', 'Meteor Shower', 'Nemo', 'Northern Lights', 'Paint Splatter', 'Pulse Pop Beats', 'Radial Sound Bar', 'Rhythmic Northern Lights', 'Romantic', 'Sound Bar', 'Streaking Notes']

nl = Nanoleaf(ip, auth_token)
panelinfo = nl.get_panel_info()
positionData = panelinfo['panelLayout']['layout']['positionData']
numberLeaves = len(positionData)

positionDict = dict()
print(numberLeaves)


#nl.set_color(PURPLE)
#effects = nl.list_effects()

nl.set_effect(effects[-1])

def formatPositions():
    for i in range(numberLeaves):
        panelId = positionData[i]['panelId']
        print(panelId)
        positionDict[str(panelId)] = [positionData[i]['x'],positionData[i]['y']]
    #print(positionDict)

def nlCoord(panelId):
    for p in range(numberLeaves):
        if (positionData[p]['panelId'] == panelId):
            print(panelId, positionData[p]['x'], positionData[p]['y'])

def event_function(event):
    #format {"events": [{"panelId": 7397, "gesture": 0}]}
    print(event)
    panelId = str(event['events'][0]['panelId'])
    if (panelId != '-1'):
        print(panelId,positionDict[panelId])

# Register for all events
formatPositions()
print("Event listener registered")
nl.register_event(event_function, [4])
