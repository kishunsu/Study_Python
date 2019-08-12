class Human:
    def __init__(self,name):
        self.set_name(name)
        
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    