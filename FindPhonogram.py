



class FindPhonogram():
    word = ""
    indexs = []
    
    def __init__(self):
        self.phonograms = {
                      "one":[],
                      "two": ["ch", "ph", "sh", "th", "ce", "cy", "ge", "gi", "gy", 
                              "ai", "ay", "ea", "ei", "ee", "ey", "ie", "oa", "ou", "ew", "ar", 
                              "er", "ir", "or", "ur", "ed", "ti", "si", "ci", "oi", "oy", "ow", "oo", 
                              "ui", "oe", "au", "aw", "al", "qu",],
                       "three": ["igh", "dge", "all", "oul", "tch", "oar", "oor", "our", "ore", "air", "are", "ear", "eer", "ier","ing"],
                       "four": ["augh", "ough", "eigh", "dger", "ture", "quet"]
                             }
        
        learnWords = ["beacouse", "beneath", "accused", "achieve", "adverse"]
        
    def setWord(self, aWord):
        self.word = aWord
        
    def getWord(self):
        
        return self.word
    
    def getIndexes(self):
        return self.indexs
    
    def patternSearch(self, length):
        wordNumber = ""
        
        """length to number"""
        if length == 1:
            wordNumber = "one"
        elif length == 2:
            wordNumber = "two"
        elif length == 3:
            wordNumber = "three"
        elif length == 4:
            wordNumber = "four"

        start = 0
        # check word long enough
        if len(self.word) < length:
            pass
        else:
            """check start to end index"""
            for index in range(len(self.word) -1):
                result = self.word[start:length]

                """check not in list"""
                for pattern in range(len(self.phonograms[wordNumber])):

                    if result == self.phonograms[wordNumber][pattern]:
                        """save index to highlight"""
                        self.indexs.append([start, length -1])
                        
                start += 1
                length += 1
        
    def scan(self):
        self.patternSearch(1)
        self.patternSearch(2)
        self.patternSearch(3)
        self.patternSearch(4)
        

       
        
        
        

finder = FindPhonogram()
finder.setWord("Because")
finder.scan()
print(finder.indexs)
"""finder.exammpleOutput(finder.getIndexes(), finder.getWord())"""



word = "because"

"""add self
start = 5
end = 4
cal = [[start, end]]

one = word[:start]
two = word[start:end+1]
three = word[end + 1:]

end = one + " " + two + " " + three
print(end)



x = []
y = []
z = x+y
print(z)

"""




