class Person(): 
    def __init__(self,age,sex):
        self.age = age
        self.sex = sex
        self.couple = None
        self.grief = False
        self.alone_time = 0
        self.child_wished = 0
        self.children = 0
    

class Couple():
    def __init__(self,man,woman):
        self.man = man
        self.woman = woman
        self.woman.couple = man
        self.man.couple = woman

    def breakup(self):
        self.man.couple = self.woman.couple = None
        self.man.grief = self.woman.grief = True
       

