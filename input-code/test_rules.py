
class Person:
    def __init__(self, firstName, lastName):
        c = 3 #caso 1 : Suspicious 
        self.d = 2
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return self.firstName + self.lastName

    def doit(self):
        b = "2+2" #caso 3: Suspicious 
        eval(b)

    def suspicious_variable_name(self):
        a = "Name dafault" #caso 3: Suspicious
        self.firstName = a
    
    def never_used_variable_op(self):
        aa = 'variable' #caso 2: Never readed
        bb = aa + 'con uso en ' #caso 3: Never readed
        cc = aa + 'sin uso' #caso 1: Never readed
        dd = 'return' #caso 3: Never readed
        return bb + dd
    
    def never_used_variable_op(self): #caso 4: Never readed
        aa = 'variable en uso en return sin operacion'
        bb = 'no uso'
        return aa


    def somethig(self):
        if True:
            print("something")
            
class Person_Data_Class: #caso 1: Data Class
    def __init__(self):
        self.name
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

class PersonDataClassWithoutMethodGet: #caso 2: Data Class
    def __init__(self):
        self.name 
    def getName(self):
        return self.name       
    #def setName(self,newName):
    #    self.name = newName

class PersonDataClassWithTwoAttribute: #caso 3: Data  Class
    def __init__(self):
        self.name   
        self.age     
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    def getAge(self):
        return self.age
    def setage(self,newName):
        self.age = newName