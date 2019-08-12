class Dog:
    def __init__(self, name):
        self.name = name
class English_Dog(Dog):
    voice="bow!"
    
    def __init__(self,name="Buddy"):
        super().__init__(name)
        
    def bark(self):
        print(self.voice)
        
    @classmethod
    def description(self):
        print(f"英語圏の犬の鳴き声は{self.voice}")
        
class Japanese_Dog(Dog):
    voice="ワン!"
    
    def __init__(self,name="ポチ"):
        super().__init__(name)
        
    def bark(self):
        print(self.voice)
        
    @classmethod
    def description(self):
        print(f"日本の犬の鳴き声は{self.voice}")
        