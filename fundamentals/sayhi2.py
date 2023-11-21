#this class has a constructor with __init__

class person:
    def __init__(self,name):
        self.name = name
    
    def sayhi(self):
        print("Hello! my name is, ", self.name)
    
p = person("Mucyo")
p.sayhi()