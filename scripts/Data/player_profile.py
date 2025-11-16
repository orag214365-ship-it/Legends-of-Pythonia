import os
import json

path = "data/UserProfile.json"
base_character = {"name": "", "class": "",
                  "level": 1, "donewithcreation": 0, "area": 1}
if not os.path.exists(path):
    os.makedirs("data", exist_ok=True)
    with open(path, "w") as f:
        json.dump(base_character, f, indent=4)

try:
    with open(path, "r") as f:
        userprofile = json.load(f)
except json.decoder.JSONDecodeError:
    with open(path, "w") as f:
        json.dump(base_character, f, indent=4)
    with open(path, "r") as f:
        userprofile = json.load(f)


def saveUserProfile():
    with open(path, "w") as f:
        json.dump(userprofile, f, indent=4)


def setToBaseProfile():
    with open(path, "w") as f:
        json.dump(base_character, f, indent=4)
