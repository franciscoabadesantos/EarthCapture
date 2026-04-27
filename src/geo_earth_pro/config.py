"""
Google Earth Pro UI Configuration
Configuration file containing pixel coordinates for UI elements in Google Earth Pro.
These coordinates are normalized to 1920x1080 resolution and automatically scaled.
"""

import pyautogui

screen_width, screen_height = pyautogui.size()

# Normalized UI coordinates for 1920x1080 resolution
# Adjust these if your screen resolution is different
UI_GEP = {
    # Window controls
    'closeTips': (1270/1920, 740/1080),
    
    # Search controls
    'searchField': (11/1920, 94/1080),
    'searchButton': (354/1920, 93/1080),
    'unpinCheck': (21/1920, 174/1080),
    
    # Zoom controls
    'zoomIn': (1875/1920, 291/1080),
    'zoomOut': (1875/1920, 412/1080),
    
    # View options
    '3dBuildings': (38/1920, 841/1080),
    
    # Save panel controls
    'savePainel': (815/1920, 63/1080),
    'savePainelOptions': (443/1920, 89/1080),
    'savePainelOptionsElement1': (412/1920, 141/1080),
    'savePainelOptionsElement2': (412/1920, 177/1080),
    'savePainelOptionsElement3': (412/1920, 209/1080),
    'savePainelOptionsElement4': (412/1920, 240/1080),
    'savePainelResolutions': (616/1920, 89/1080),
    'savePainelResolutionCurrent': (600/1920, 115/1080),
    'savePainelResolutionMax': (600/1920, 257/1080),
    'savePainelSave': (763/1920, 90/1080),
    'selectFolder': (1031/1920, 162/1080),
    'saveFile': (1144/1920, 665/1080),
    'cancelFile': (1268/1920, 665/1080),
    
    # History controls
    'historyButton': (609/1920, 63/1080),
    'historyUpdateDate': (668/1920, 107/1080),
    'historyOpionsDate': (703/1920, 93/1080),
    'historyGetDate': (905/1920, 412/1080),
    'historyCloseOptionsDate': (1190/1920, 303/1080),
    'moveBackHistory': (427/1920, 121/1080),
    'moveforwaardHistory': (699/1920, 121/1080),
    
    # Pin controls
    'pinSelectRightClick': (130/1920, 170/1080),
    'pinSave': (220/1920, 260/1080),
    'pinUnpinEverything': (25/1920, 372/1080)
}

# Scale coordinates to current screen resolution
UI_GEP_SCREEN_SIZED = {
    key: (coord[0] * screen_width, coord[1] * screen_height) 
    for key, coord in UI_GEP.items()
}

# Output folder for downloaded images
# Update this path to where you want images saved
IMAGES_FOLDER = './output'

# Number of history steps to go back
HISTORY_STEPS = 3

# Pause between actions (in seconds)
PAUSE_BETWEEN_ACTIONS = 3
