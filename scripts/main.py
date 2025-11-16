from GUI.gui import startScreen
from GUI.charachter_creation import chooseClass, chooseName, confirmUserData
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
