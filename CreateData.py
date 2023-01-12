



class CreateData:

    def createEmptyPeel(self):
        peel = {}
        peel["entry"] = []

        return peel

    def createEmptyEntry(self):
        entry = {
                "name": "",
                "number": "",
                "point": "",
                "Evidence": {
                            "citation": "",
                            "reference": ""
                            },
                "Expand": "",
                "link": "",
                "notes": "",
        }

        return entry

    def printModel(self, model):
        print(model)

create = CreateData()
create.createEmptyPeel()

