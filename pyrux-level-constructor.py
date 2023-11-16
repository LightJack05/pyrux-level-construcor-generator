import json

with open("LevelData.json") as file:
    content = file.read()
    file.close()

importedObject = json.loads(content)
print()

ob = "{"
cb = "}"


def escape(string):
    return string.replace("\r", "\\r")


constructor = f"""
new(
    "{escape(importedObject["LevelName"])}",
    "{escape(importedObject["Task"])}",
    true,
    new(
        new bool[{importedObject["MapLayout"]["SizeX"]}, {importedObject["MapLayout"]["SizeY"]}]{json.dumps(importedObject["MapLayout"]["WallLayout"]).replace("[","{").replace("]","}")},
        new int[{importedObject["MapLayout"]["SizeX"]}, {importedObject["MapLayout"]["SizeY"]}]{json.dumps(importedObject["MapLayout"]["CollectablesLayout"]).replace("[","{").replace("]","}")},
        new({importedObject["MapLayout"]["CurrentPlayerPosition"]["X"]},{importedObject["MapLayout"]["CurrentPlayerPosition"]["Y"] }),
        {importedObject["MapLayout"]["CurrentPlayerDirection"]}
    ),
    "{escape(importedObject["Script"])}",
    "{escape(importedObject["Hint"])}",
    {str(importedObject["Completed"]).lower()},
    new(
        new bool[{importedObject["GoalMapLayout"]["SizeX"]}, {importedObject["GoalMapLayout"]["SizeY"]}]{json.dumps(importedObject["GoalMapLayout"]["WallLayout"]).replace("[","{").replace("]","}")},
        new int[{importedObject["GoalMapLayout"]["SizeX"]}, {importedObject["GoalMapLayout"]["SizeY"]}]{json.dumps(importedObject["GoalMapLayout"]["CollectablesLayout"]).replace("[","{").replace("]","}")},
        new({importedObject["GoalMapLayout"]["CurrentPlayerPosition"]["X"]},{importedObject["GoalMapLayout"]["CurrentPlayerPosition"]["Y"] }),
        {importedObject["GoalMapLayout"]["CurrentPlayerDirection"]}
    )
)
"""
print(constructor)
