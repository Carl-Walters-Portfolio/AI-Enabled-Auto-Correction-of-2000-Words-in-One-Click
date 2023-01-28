
import json

class File:
    """
    Provides the ability to easily create and read various files.
    """
    def readJsonFile(self, name):
        """
        Read json file

        Args:
            name (Str): _description_

        Returns:
            Json: Returns file called name + ".json" from this Directory
        """
        
        with open(name + ".json") as json_file:
            data = json.load(json_file)

        return data

    def createJsonfile(self, name, data):
        """
        Creates .json file with name and data provided

        Args:
            name (str): Provides name for file.
            data (Str): Data to be provided For the files content when created.
        """
        with open(name + ".json", 'w') as outfile:
            json.dump(data, outfile, indent=5)

    def createTextFile(self, fileName, text):
        """
        Creates .text file with name and data provided

        Args:
            fileName (str): Provides name for file.
            text (Str): Data to be provided For the files content when created.
        """
        with open(fileName + ".text", 'w') as f:
            f.write(text)


