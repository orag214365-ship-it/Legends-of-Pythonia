
from Data.player_profile import userprofile
import os
import json

path = "data/UserStats.json"
base_stats = {"changeable_stats": {"attack": 7,
                                   "defense": 6,
                                   "speed": 6,
                                   "health": 10,
                                   "mana": 53},
              "normal_stats": {"attack": 7,
                               "defense": 6,
                               "speed": 6,
                               "health": 10,
                               "mana": 53}}

if not os.path.exists(path):
    os.makedirs("data", exist_ok=True)
    with open(path, "w") as f:
        json.dump(base_stats, f, indent=4)

try:
    with open(path, "r") as f:
        userstats = json.load(f)
except json.decoder.JSONDecodeError:
    with open(path, "w") as f:
        json.dump(base_stats, f, indent=4)
    with open(path, "r") as f:
        userstats = json.load(f)


def saveUserStats():
    with open(path, "w") as f:
        json.dump(base_stats, f, indent=4)


def setToBaseStats():
    with open(path, "w") as f:
        json.dump(base_stats, f, indent=4)


def setClassStats():
    if userprofile["class"] == "warrior":
        increase = {
            "attack": 14,
            "defense": 67,
            "speed": -33,
            "health": 20,
            "mana": -62
        }
        for key, value in base_stats["changeable_stats"].items():
            if key in increase:
                base_stats["changeable_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
        for key, value in base_stats["normal_stats"].items():
            if key in increase:
                base_stats["normal_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()

    elif userprofile["class"] == "rogue":
        increase = {
            "attack": 0,
            "defense": -33,
            "speed": 67,
            "health": -10,
            "mana": -43
        }
        for key, value in base_stats["changeable_stats"].items():
            if key in increase:
                base_stats["changeable_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
        for key, value in base_stats["normal_stats"].items():
            if key in increase:
                base_stats["normal_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
    elif userprofile["class"] == "mage":
        increase = {
            "attack": 43,
            "defense": -50,
            "speed": -17,
            "health": -30,
            "mana": 126
        }
        for key, value in base_stats["changeable_stats"].items():
            if key in increase:
                base_stats["changeable_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
        for key, value in base_stats["normal_stats"].items():
            if key in increase:
                base_stats["normal_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
    elif userprofile["class"] == "archer":
        increase = {
            "attack": 14,
            "defense": -17,
            "speed": 33,
            "health": -10,
            "mana": -25
        }
        for key, value in base_stats["changeable_stats"].items():
            if key in increase:
                base_stats["changeable_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
        for key, value in base_stats["normal_stats"].items():
            if key in increase:
                base_stats["normal_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
    elif userprofile["class"] == "tank":
        increase = {
            "attack": -29,
            "defense": 100,
            "speed": -50,
            "health": 50,
            "mana": -81
        }
        for key, value in base_stats["changeable_stats"].items():
            if key in increase:
                base_stats["changeable_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
        for key, value in base_stats["normal_stats"].items():
            if key in increase:
                base_stats["normal_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
    elif userprofile["class"] == "summoner":
        increase = {
            "attack": -14,
            "defense": -33,
            "speed": -17,
            "health": -20,
            "mana": 185
        }
        for key, value in base_stats["changeable_stats"].items():
            if key in increase:
                base_stats["changeable_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
        for key, value in base_stats["normal_stats"].items():
            if key in increase:
                base_stats["normal_stats"][key] = value + \
                    (value * increase[key] // 100)
                saveUserStats()
