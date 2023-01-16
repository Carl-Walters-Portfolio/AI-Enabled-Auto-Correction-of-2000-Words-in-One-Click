
import json

class File:
    def readJsonFile(self, name):
        with open(name + ".json") as json_file:
            data = json.load(json_file)

        return data

    def createJsonfile(self, name, data):
        with open(name + ".json", 'w') as outfile:
            json.dump(data, outfile, indent=5)

    def readTextFile(self):
        pass

    def createTextFile(self, fileName, text):
        with open(fileName + ".text", 'w') as f:
            f.write(text)


