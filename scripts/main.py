from GUI.gui import startScreen, testScreen, tutorial
from GUI.charachter_creation import chooseClass, chooseName, confirmUserData
from GUI.gui_classes import Button, Entry, DialogueBox
from Data.player_profile import saveUserProfile, userprofile
from Data.player_stats import setClassStats

startScreen()
if not userprofile["donewithcreation"]:
    while True:
        chooseName()
        chooseClass()
        if confirmUserData():
            userprofile["donewithcreation"] = 1
            saveUserProfile()
            setClassStats()
            break
        else:
            continue

if userprofile["area"] == 1:
    tutorial()
